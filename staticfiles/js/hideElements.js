function hideAllChildren(children) {
    Array.prototype.forEach.call(children, (item) => {
        item.classList.add('hiddenRow');
        item.classList.remove('opened');
        let childId = item.id
        let nextChildrenClassName = childId.replace('employee', 'manager')
        let nextChildren = tableOrderTotal.getElementsByClassName(nextChildrenClassName);
        if (nextChildren.length != 0) hideAllChildren(nextChildren);
    });
}

function unhideAllChildren(children) {
    Array.prototype.forEach.call(children, (item) => {
        item.classList.remove('hiddenRow');
    });
}