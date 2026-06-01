class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stack = new Stack<String>();
        for(int i = 0; i<tokens.length; i++){
            System.out.println(stack);
            int first;
            int second;
            switch(tokens[i]){
                case "+":
                    first = Integer.parseInt(stack.pop());
                    second = Integer.parseInt(stack.pop());
                    stack.push(first + second + "");
                    break;
                case "-":
                    first = Integer.parseInt(stack.pop());
                    second = Integer.parseInt(stack.pop());
                    stack.push(second - first + "");
                    break;
                case "*":
                    first = Integer.parseInt(stack.pop());
                    second = Integer.parseInt(stack.pop());
                    stack.push(first * second+ "");
                    break;
                case "/":
                    first = Integer.parseInt(stack.pop());
                    second = Integer.parseInt(stack.pop());
                    if (first == 0) return -1;
                    stack.push((second/ first) + "");
                    break;
                default:
                    stack.push(tokens[i]);
                    break;
                
            }
        }
        return Integer.parseInt(stack.pop());
    }
}
