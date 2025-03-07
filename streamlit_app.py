from queue import Full


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": Full,
   "id": "e0793801-5be1-4a46-a2cd-2ab5c86c053e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import panel as pn\n",
    "\n",
    "pn.extension(template='material')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": Full,
   "id": "8d9ec6ce-c405-4dd9-960e-35bd7ea95d4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "number = pn.widgets.IntSlider(value=3, start=0, end=10, name='number')\n",
    "size = pn.widgets.IntSlider(value=10, start=10, end=25, step=5, name='size')\n",
    "\n",
    "pn.Column(\n",
    "    number, size,\n",
    "    pn.pane.Markdown(\n",
    "        pn.bind(lambda n: \"⭐\" * n, number),\n",
    "        styles=pn.bind(lambda size: {'font-size': f'{size}px'}, size)\n",
    "    )\n",
    ").servable(title='Our Simple App')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-panel-2023.05-py310",
   "language": "python",
   "name": "conda-env-anaconda-panel-2023.05-py310-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}