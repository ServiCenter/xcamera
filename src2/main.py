from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.uix.camera import Camera
from kivy.lang import Builder
from jnius import autoclass
import numpy as np
import cv2


CameraInfo = autoclass('android.hardware.Camera$CameraInfo')
CAMERA_INDEX = {'front': CameraInfo.CAMERA_FACING_FRONT, 'back': CameraInfo.CAMERA_FACING_BACK}
Builder.load_file("myapplayout.kv")


class AndroidCamera(Camera):
    resolution = (640, 480)
    index = CAMERA_INDEX['back']
    counter = 0

    def on_tex(self, *l):
        if self._camera._buffer is None:
            return None

        super(AndroidCamera, self).on_tex(*l)
        self.texture = Texture.create(size=np.flip(self.resolution), colorfmt='rgb')
        frame = self.frame_from_buf()
        self.frame_to_screen(frame)

    def frame_from_buf(self):
        w, h = self.resolution
        frame = np.frombuffer(self._camera._buffer.tostring(), 'uint8').reshape((h + h // 2, w))
        frame_bgr = cv2.cvtColor(frame, 93)
        if self.index:
            return np.flip(np.rot90(frame_bgr, 1), 1)
        else:
            return np.rot90(frame_bgr, 3)

    def frame_to_screen(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(frame_rgb, str(self.counter), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        self.counter += 1
        flipped = np.flip(frame_rgb, 0)
        buf = flipped.tobytes()
        self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')


class MyLayout(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.uix.camera import Camera
from kivy.lang import Builder
from jnius import autoclass
import numpy as np
import cv2


CameraInfo = autoclass('android.hardware.Camera$CameraInfo')
CAMERA_INDEX = {'front': CameraInfo.CAMERA_FACING_FRONT, 'back': CameraInfo.CAMERA_FACING_BACK}
Builder.load_file("myapplayout.kv")


class AndroidCamera(Camera):
    resolution = (640, 480)
    index = CAMERA_INDEX['back']
    counter = 0

    def on_tex(self, *l):
        if self._camera._buffer is None:
            return None

        super(AndroidCamera, self).on_tex(*l)
        self.texture = Texture.create(size=np.flip(self.resolution), colorfmt='rgb')
        frame = self.frame_from_buf()
        self.frame_to_screen(frame)

    def frame_from_buf(self):
        w, h = self.resolution
        frame = np.frombuffer(self._camera._buffer.tostring(), 'uint8').reshape((h + h // 2, w))
        frame_bgr = cv2.cvtColor(frame, 93)
        if self.index:
            return np.flip(np.rot90(frame_bgr, 1), 1)
        else:
            return np.rot90(frame_bgr, 3)

    def frame_to_screen(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(frame_rgb, str(self.counter), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        self.counter += 1
        flipped = np.flip(frame_rgb, 0)
        buf = flipped.tobytes()
        self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')


class MyLayout(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()