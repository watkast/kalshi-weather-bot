# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 12:51 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 105 | 103 | 34 (33%) | 39¢ | 47% | -$79.93 | -19% |
| Silver | 53 | 52 | 16 (31%) | 34¢ | 42% | -$23.75 | -13% |
| Gold | 52 | 51 | 18 (35%) | 45¢ | 52% | -$56.18 | -24% |

*Earlier half -$40.94 / later half -$38.99.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 106 | 35 (33%) | -$92.31 | -21% |
| 4¢+ ← live bot | 103 | 36 (35%) | -$24.22 | -6% |
| 6¢+ | 91 | 37 (41%) | $60.78 | +20% |
| 8¢+ | 78 | 33 (42%) | $82.01 | +33% |
| 10¢+ | 65 | 24 (37%) | $42.33 | +21% |
| 15¢+ | 38 | 13 (34%) | $33.53 | +35% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2640 | -1.7% |
| Hyperliquid price vs Kalshi's target | 2640 | +1.4% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:46:21 PM | Gold | UP | 13.7 min | 41¢ | 50% | 7¢ | Open | — |
| 9/29 12:46:03 PM | Silver | UP | 13.9 min | 39¢ | 50% | 9¢ | Open | — |
| 9/29 12:33:37 PM | Gold | UP | 11.4 min | 24¢ | 35% | 10¢ | ✅ Won | $7.47 |
| 9/29 12:32:31 PM | Silver | UP | 12.5 min | 32¢ | 39% | 5¢ | ✅ Won | $6.64 |
| 9/29 12:22:09 PM | Silver | UP | 7.8 min | 29¢ | 39% | 9¢ | ❌ Lost | -$3.05 |
| 9/29 12:16:11 PM | Gold | DOWN | 13.8 min | 36¢ | 44% | 6¢ | ✅ Won | $6.23 |
| 9/29 12:01:02 PM | Gold | UP | 13.9 min | 91¢ | 96% | 4¢ | ✅ Won | $0.84 |
| 9/29 11:47:34 AM | Silver | UP | 12.4 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/29 11:46:56 AM | Gold | UP | 13.1 min | 40¢ | 47% | 5¢ | ❌ Lost | -$4.17 |
| 9/29 11:32:32 AM | Gold | UP | 12.4 min | 34¢ | 46% | 10¢ | ❌ Lost | -$3.56 |
| 9/29 11:32:10 AM | Silver | UP | 12.8 min | 32¢ | 41% | 7¢ | ❌ Lost | -$3.36 |
| 9/29 11:19:27 AM | Gold | DOWN | 10.5 min | 35¢ | 41% | 5¢ | ❌ Lost | -$3.66 |
