import maya.cmds as cmds

# หากโค้ดนี้อยู่ในไฟล์ RunRT.py และถูกเรียกจาก main.py ที่ใช้ PySide, 
# QtWidgets จะต้องถูกเรียกใช้ผ่าน 'self' หรือถูก import ไว้ที่นี่

def RunRotateAxes(self):
    """
    หมุน LRA Component หรือ Object ที่ถูกเลือก โดยใช้ค่าจาก UI Checkbox
    เทียบเท่ากับ MEL: rotate -r -os -p 0 0 0;
    """
    
    # ในการใช้ QMessageBox ใน RunRT.py คุณต้องแน่ใจว่าได้เข้าถึง QtWidgets 
    # ผ่าน self.QtWidgets หรือ import ไว้ (จะสมมติว่าคุณจัดการการ import แล้ว)
    try:
        QtWidgets = self.QtWidgets 
    except:
        # Fallback หากไม่มีการเข้าถึง self.QtWidgets (อาจต้องแก้ที่ main.py)
        try:
            from PySide6 import QtWidgets
        except ImportError:
            try:
                from PySide2 import QtWidgets
            except ImportError:
                # ถ้าหาไม่เจอ ให้ใช้ cmds.warning แทน
                def warning_fallback(self, title, message):
                    cmds.warning(f"{title}: {message}")
                QtWidgets = type('FakeQtWidgets', (), {'QMessageBox': type('FakeQMessageBox', (), {'warning': warning_fallback})})

    sel = cmds.ls(selection=True)
    if not sel:
        QtWidgets.QMessageBox.warning(None, "No Selection", "Please select an object or LRA component to rotate.")
        return

    # 1. คำนวณองศารวม
    deg_sum = 0
    if self.RTcheckBox90.isChecked(): deg_sum += 90
    if self.RTcheckBox180.isChecked(): deg_sum += 180
    if hasattr(self, "RTcheckBox270") and self.RTcheckBox270.isChecked(): deg_sum += 270

    if deg_sum == 0:
        QtWidgets.QMessageBox.warning(None, "No Angle", "Please select a rotation degree (90, 180, or 270).")
        return

    # 2. กำหนดค่าการหมุนสำหรับแกน X, Y, Z
    axes_str = []
    rot_x = deg_sum if self.RTcheckBoxX.isChecked() else 0
    rot_y = deg_sum if self.RTcheckBoxY.isChecked() else 0
    rot_z = deg_sum if self.RTcheckBoxZ.isChecked() else 0
    
    if self.RTcheckBoxX.isChecked(): axes_str.append("X")
    if self.RTcheckBoxY.isChecked(): axes_str.append("Y")
    if self.RTcheckBoxZ.isChecked(): axes_str.append("Z")

    if not axes_str:
        QtWidgets.QMessageBox.warning(None, "No Axis", "Please select an axis (X, Y, or Z).")
        return

    # 3. ใช้ cmds.rotate() เพื่อทำการหมุน
    try:
        # - relative=True (r): หมุนแบบเพิ่มค่าจากปัจจุบัน
        # - objectSpace=True (os): หมุนใน Object Space (Local Space)
        # - pivot=(0, 0, 0) (p/fo): หมุนรอบตัวเอง (เทียบเท่า -fo 0 0 0)
        cmds.rotate(
            rot_x, rot_y, rot_z, 
            relative=True, 
            objectSpace=True, 
            pivot=(0, 0, 0)
        )
        
        # 4. ล้าง Checkbox เพื่อ UX ที่ดี
        self.RTcheckBoxX.setChecked(False)
        self.RTcheckBoxY.setChecked(False)
        self.RTcheckBoxZ.setChecked(False)
        self.RTcheckBox90.setChecked(False)
        self.RTcheckBox180.setChecked(False)
        if hasattr(self, "RTcheckBox270"): 
            self.RTcheckBox270.setChecked(False)
            
        cmds.inViewMessage(amg=f"<hl>Rotated LRA:</hl> {', '.join(axes_str)} {deg_sum}°", pos='midCenter', fade=True)
        
    except Exception as e:
        QtWidgets.QMessageBox.warning(None, "Rotation Error", f"Rotation failed. Ensure you have the correct component selected:\n{e}")