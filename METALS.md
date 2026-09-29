# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 3:22 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 48 | 46 | 16 (35%) | 39¢ | 47% | -$26.28 | -14% |
| Silver | 24 | 23 | 7 (30%) | 33¢ | 42% | -$10.42 | -13% |
| Gold | 24 | 23 | 9 (39%) | 44¢ | 52% | -$15.86 | -15% |

*Earlier half $19.67 / later half -$45.95.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 47 | 12 (26%) | -$75.94 | -39% |
| 4¢+ ← live bot | 45 | 13 (29%) | -$32.74 | -20% |
| 6¢+ | 41 | 13 (32%) | $0.98 | +1% |
| 8¢+ | 36 | 12 (33%) | $19.18 | +19% |
| 10¢+ | 31 | 8 (26%) | $1.75 | +2% |
| 15¢+ | 16 | 5 (31%) | $15.52 | +45% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1155 | -6.8% |
| Hyperliquid price vs Kalshi's target | 1155 | -11.9% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:22:33 AM | Silver | UP | 7.5 min | 56¢ | 66% | 8¢ | Open | — |
| 9/29 3:16:18 AM | Gold | DOWN | 13.7 min | 39¢ | 50% | 9¢ | Open | — |
| 9/29 3:04:34 AM | Silver | DOWN | 10.4 min | 32¢ | 40% | 7¢ | ✅ Won | $6.64 |
| 9/29 3:02:03 AM | Gold | DOWN | 12.9 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |
| 9/29 12:33:04 AM | Gold | DOWN | 11.9 min | 33¢ | 42% | 7¢ | ❌ Lost | -$3.46 |
| 9/29 12:31:29 AM | Silver | DOWN | 13.5 min | 34¢ | 40% | 4¢ | ❌ Lost | -$3.56 |
| 9/29 12:16:42 AM | Silver | UP | 13.3 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/29 12:16:24 AM | Gold | UP | 13.6 min | 28¢ | 37% | 8¢ | ❌ Lost | -$2.95 |
| 9/29 12:03:03 AM | Gold | DOWN | 11.9 min | 36¢ | 45% | 7¢ | ❌ Lost | -$3.77 |
| 9/29 12:03:03 AM | Silver | DOWN | 11.9 min | 12¢ | 18% | 5¢ | ❌ Lost | -$1.28 |
| 9/28 11:46:05 PM | Gold | UP | 13.9 min | 28¢ | 34% | 5¢ | ✅ Won | $7.05 |
| 9/28 11:46:05 PM | Silver | UP | 13.9 min | 33¢ | 42% | 8¢ | ❌ Lost | -$3.46 |
