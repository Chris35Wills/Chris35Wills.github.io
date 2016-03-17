---
---

# Creating multiple figures

The idea of creating specific access to the figure and axis objects allude to [here](../matplotlib_3d) are extremely useful when you want to start creating multiple plots in a single figure.

When we were creating figures earlier on, we were just calling things like this:

```python
plt.scatter(x,y,z)
plt.show()
```

This worked fine as python gives you access directly to the attributes of the current figure and current axis that you are creating - the problem is, you can't actually get a direct hold on the axis object which limits your ability to customise it. To create 



