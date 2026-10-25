# Range-Scalp Bot

*Updated Sun Oct 25 07:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32756 | 28563 | 4193 (42) | 5 | $-9318.65 | -4.5% |
| **+10¢** | 24525 | 19671 | 4854 (60) | 6 | $-8317.89 | -5.4% |
| **+15¢** | 20534 | 15311 | 5223 (83) | 6 | $-7479.98 | -5.8% |
| **+20¢** | 18190 | 12722 | 5468 (105) | 7 | $-6626.79 | -5.8% |
| **+10¢ (15¢ stop)** | 40240 | 40180 | 60 (32) | 2 | $-15373.88 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 07:25 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 10-25 07:25 | +20 | ZEC | DOWN | 0.68 | open |  |
| 10-25 07:25 | +15 | ZEC | DOWN | 0.68 | open |  |
| 10-25 07:25 | +10 | ZEC | DOWN | 0.68 | open |  |
| 10-25 07:25 | +5 | ZEC | DOWN | 0.68 | open |  |
| 10-25 07:25 | +10 stop | NEAR | UP | 0.70 | open |  |
| 10-25 07:25 | +10 stop | BTC | DOWN | 0.51 | 0.65 | 1.06 |
| 10-25 07:25 | +10 stop | SOL | DOWN | 0.42 | 0.57 | 1.14 |
| 10-25 07:23 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 10-25 07:23 | +10 stop | XRP | UP | 0.59 | 0.76 | 1.40 |
| 10-25 07:23 | +20 | XRP | UP | 0.59 | 0.88 | 2.65 |
| 10-25 07:23 | +15 | XRP | UP | 0.59 | 0.76 | 1.40 |
| 10-25 07:23 | +10 | XRP | UP | 0.59 | 0.76 | 1.40 |
| 10-25 07:23 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 10-25 07:23 | +5 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-25 07:23 | +5 | BNB | UP | 0.50 | 0.55 | 0.14 |
| 10-25 07:22 | +10 stop | NEAR | DOWN | 0.59 | 0.77 | 1.54 |
| 10-25 07:22 | +10 stop | BTC | DOWN | 0.53 | 0.69 | 1.27 |
| 10-25 07:21 | +10 stop | ETH | DOWN | 0.55 | 0.68 | 0.96 |
| 10-25 07:21 | +10 stop | SOL | UP | 0.67 | 0.48 | -2.24 |
| 10-25 07:21 | +10 | SOL | UP | 0.67 | open |  |
| 10-25 07:21 | +5 | SOL | UP | 0.66 | open |  |
| 10-25 07:21 | +10 stop | HYPE | DOWN | 0.56 | 0.79 | 2.04 |
| 10-25 07:19 | +5 | BNB | UP | 0.67 | 0.73 | 0.30 |
| 10-25 07:19 | +10 stop | BTC | UP | 0.58 | 0.42 | -1.96 |
| 10-25 07:19 | +20 | BTC | UP | 0.58 | open |  |
| 10-25 07:19 | +15 | BTC | UP | 0.58 | open |  |
| 10-25 07:19 | +10 | BTC | UP | 0.59 | open |  |
| 10-25 07:19 | +5 | BTC | UP | 0.59 | open |  |
| 10-25 07:18 | +5 | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 10-25 07:18 | +5 | DOGE | UP | 0.63 | open |  |
| 10-25 07:18 | +10 stop | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-25 07:18 | +20 | SOL | UP | 0.60 | open |  |
| 10-25 07:18 | +15 | SOL | UP | 0.60 | open |  |
| 10-25 07:18 | +10 | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-25 07:18 | +5 | SOL | UP | 0.60 | 0.66 | 0.27 |
| 10-25 07:18 | +10 stop | BNB | UP | 0.65 | 0.38 | -3.03 |
| 10-25 07:18 | +20 | BNB | UP | 0.65 | open |  |
| 10-25 07:18 | +15 | BNB | UP | 0.65 | open |  |
| 10-25 07:18 | +10 | BNB | UP | 0.65 | open |  |
