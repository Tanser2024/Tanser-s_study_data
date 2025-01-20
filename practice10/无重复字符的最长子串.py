def trap( height):
    mount = max(height)
    mount1 = height.index(mount);
    mount2 = height.rindex(mount)
    cur = 0;
    cur_set = 0;
    s = 0
    for i in range(mount1):
        if height[i] > cur:
            s += (i - cur_set) * cur
            cur_set = i;
            cur = height[i]
    s += (mount2 - mount1 + 1) * mount
    if mount2 + 1 == len(height):
        return s - sum(height)
    cur = height[mount2 + 1];
    cur_set = mount2 + 1
    for i in range(mount2 + 1, len(height)):
        if height[i] < cur:
            s += (i - cur_set) * cur
            cur_set = i;
            cur = height[i]
    return s - sum(height)
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))