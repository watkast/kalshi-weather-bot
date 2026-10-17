# Range-Scalp Bot

*Updated Sat Oct 17 00:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20082 | 17461 | 2621 (29) | 3 | $-5988.08 | -4.7% |
| **+10¢** | 15122 | 12094 | 3028 (41) | 4 | $-5385.01 | -5.7% |
| **+15¢** | 12646 | 9389 | 3257 (60) | 5 | $-4884.32 | -6.2% |
| **+20¢** | 11211 | 7802 | 3409 (79) | 8 | $-4318.08 | -6.1% |
| **+10¢ (15¢ stop)** | 24693 | 24643 | 50 (29) | 3 | $-9398.21 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 00:07 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-17 00:07 | +10 stop | ZEC | UP | 0.68 | 0.81 | 1.03 |
| 10-17 00:07 | +5 | ZEC | UP | 0.68 | 0.76 | 0.51 |
| 10-17 00:07 | +10 stop | SOL | DOWN | 0.54 | open |  |
| 10-17 00:07 | +15 | SOL | DOWN | 0.54 | open |  |
| 10-17 00:07 | +10 | SOL | DOWN | 0.54 | open |  |
| 10-17 00:07 | +5 | SOL | DOWN | 0.54 | open |  |
| 10-17 00:05 | +5 | BTC | DOWN | 0.65 | open |  |
| 10-17 00:04 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 10-17 00:03 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-17 00:02 | +10 stop | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-17 00:02 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-17 00:02 | +15 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-17 00:02 | +10 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-17 00:02 | +5 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-17 00:02 | +10 stop | NEAR | DOWN | 0.68 | 0.53 | -1.84 |
| 10-17 00:02 | +20 | NEAR | DOWN | 0.68 | open |  |
| 10-17 00:02 | +15 | NEAR | DOWN | 0.68 | open |  |
| 10-17 00:02 | +10 | NEAR | DOWN | 0.68 | open |  |
| 10-17 00:02 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 10-17 00:02 | +10 stop | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 00:02 | +20 | XRP | DOWN | 0.71 | open |  |
| 10-17 00:02 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 00:02 | +10 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 00:02 | +5 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-17 00:02 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-17 00:02 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-17 00:02 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-17 00:02 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-17 00:02 | +5 | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 10-17 00:02 | +10 stop | ZEC | DOWN | 0.70 | 0.50 | -2.33 |
| 10-17 00:02 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-17 00:02 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-17 00:02 | +10 | ZEC | DOWN | 0.70 | open |  |
| 10-17 00:02 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-17 00:01 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 00:01 | +20 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-17 00:01 | +15 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-17 00:01 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 00:01 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.38 |
