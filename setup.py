from setuptools import setup

setup(
   name="imagerytools",
   version="0.0",
   description="Satellite Imagery Analysis package",
   author="Minerva Sats / Remote Sensing Team",
   author_email="henrique.albagli@gmail.com",
   install_requires=['imutils', 'numpy', 'opencv-python',],
   packages=['imagerytools',],
)
