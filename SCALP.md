# Range-Scalp Bot

*Updated Sat Oct 03 07:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 365 | 311 | 54 (1) | 4 | $-149.05 | -6.4% |
| **+10¢** | 292 | 233 | 59 (1) | 5 | $-114.53 | -6.2% |
| **+15¢** | 244 | 181 | 63 (1) | 5 | $-117.37 | -7.6% |
| **+20¢** | 208 | 142 | 66 (1) | 7 | $-129.43 | -9.8% |
| **+10¢ (15¢ stop)** | 496 | 496 | 0 (0) | 5 | $-258.75 | -8.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 07:06 | +10 stop | SOL | DOWN | 0.63 | open |  |
| 10-03 07:06 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-03 07:06 | +10 | SOL | DOWN | 0.63 | open |  |
| 10-03 07:06 | +5 | SOL | DOWN | 0.63 | open |  |
| 10-03 07:04 | +5 | HYPE | UP | 0.67 | open |  |
| 10-03 07:03 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 10-03 07:03 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 10-03 07:03 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-03 07:03 | +10 | BNB | DOWN | 0.67 | open |  |
| 10-03 07:03 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.33 |
| 10-03 07:03 | +10 stop | HYPE | UP | 0.62 | open |  |
| 10-03 07:03 | +20 | HYPE | UP | 0.62 | open |  |
| 10-03 07:03 | +15 | HYPE | UP | 0.62 | open |  |
| 10-03 07:03 | +10 | HYPE | UP | 0.62 | open |  |
| 10-03 07:03 | +5 | HYPE | UP | 0.62 | 0.67 | 0.17 |
| 10-03 07:03 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.95 |
| 10-03 07:03 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.95 |
| 10-03 07:03 | +5 | ZEC | DOWN | 0.67 | 0.79 | 0.95 |
| 10-03 07:03 | +10 stop | XRP | DOWN | 0.60 | 0.77 | 1.40 |
| 10-03 07:03 | +20 | XRP | DOWN | 0.60 | 0.80 | 1.71 |
| 10-03 07:03 | +15 | XRP | DOWN | 0.60 | 0.77 | 1.40 |
| 10-03 07:03 | +10 | XRP | DOWN | 0.60 | 0.77 | 1.40 |
| 10-03 07:03 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 10-03 07:02 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-03 07:02 | +20 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-03 07:02 | +15 | ZEC | DOWN | 0.61 | 0.79 | 1.51 |
| 10-03 07:02 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-03 07:02 | +5 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-03 07:02 | +10 stop | BNB | DOWN | 0.55 | 0.71 | 1.27 |
| 10-03 07:02 | +20 | BNB | DOWN | 0.55 | open |  |
| 10-03 07:02 | +15 | BNB | DOWN | 0.55 | 0.71 | 1.27 |
| 10-03 07:02 | +10 | BNB | DOWN | 0.55 | 0.71 | 1.27 |
| 10-03 07:02 | +5 | BNB | DOWN | 0.55 | 0.71 | 1.27 |
| 10-03 07:02 | +5 | ETH | UP | 0.56 | open |  |
| 10-03 07:01 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-03 07:01 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-03 07:01 | +15 | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 10-03 07:01 | +10 | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 10-03 07:01 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 10-03 07:01 | +10 stop | ETH | UP | 0.56 | open |  |
