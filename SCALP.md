# Range-Scalp Bot

*Updated Wed Oct 07 13:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6447 | 5607 | 840 (9) | 5 | $-1873.92 | -4.6% |
| **+10¢** | 4897 | 3909 | 988 (16) | 5 | $-1752.47 | -5.7% |
| **+15¢** | 4112 | 3068 | 1044 (20) | 8 | $-1459.22 | -5.7% |
| **+20¢** | 3677 | 2583 | 1094 (27) | 7 | $-1191.19 | -5.2% |
| **+10¢ (15¢ stop)** | 7820 | 7805 | 15 (9) | 3 | $-2733.70 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 13:08 | +10 stop | NEAR | DOWN | 0.71 | 0.54 | -2.02 |
| 10-07 13:07 | +10 stop | BTC | UP | 0.65 | open |  |
| 10-07 13:07 | +10 stop | ZEC | UP | 0.65 | open |  |
| 10-07 13:07 | +20 | ZEC | UP | 0.65 | open |  |
| 10-07 13:07 | +15 | ZEC | UP | 0.65 | open |  |
| 10-07 13:07 | +10 stop | SOL | UP | 0.62 | 0.73 | 0.79 |
| 10-07 13:06 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.03 |
| 10-07 13:06 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-07 13:06 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-07 13:06 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-07 13:06 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 10-07 13:06 | +5 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-07 13:05 | +10 stop | ZEC | UP | 0.62 | 0.75 | 1.00 |
| 10-07 13:05 | +10 stop | SOL | DOWN | 0.66 | 0.47 | -2.24 |
| 10-07 13:04 | +10 stop | DOGE | DOWN | 0.64 | 0.47 | -2.05 |
| 10-07 13:04 | +10 stop | BTC | DOWN | 0.55 | 0.39 | -1.95 |
| 10-07 13:04 | +10 stop | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-07 13:04 | +10 stop | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-07 13:04 | +10 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-07 13:04 | +5 | HYPE | UP | 0.64 | 0.73 | 0.55 |
| 10-07 13:03 | +10 stop | BNB | UP | 0.67 | 0.47 | -2.34 |
| 10-07 13:03 | +15 | BNB | UP | 0.67 | open |  |
| 10-07 13:03 | +10 | BNB | UP | 0.67 | open |  |
| 10-07 13:03 | +5 | BNB | UP | 0.67 | open |  |
| 10-07 13:03 | +10 stop | SOL | UP | 0.63 | 0.47 | -1.95 |
| 10-07 13:03 | +15 | SOL | UP | 0.63 | open |  |
| 10-07 13:03 | +10 | SOL | UP | 0.63 | 0.73 | 0.69 |
| 10-07 13:03 | +5 | SOL | UP | 0.63 | 0.73 | 0.69 |
| 10-07 13:03 | +5 | DOGE | UP | 0.62 | open |  |
| 10-07 13:03 | +10 stop | BTC | UP | 0.67 | 0.42 | -2.84 |
| 10-07 13:03 | +10 stop | ZEC | UP | 0.70 | 0.48 | -2.53 |
| 10-07 13:03 | +10 stop | DOGE | UP | 0.59 | 0.32 | -3.03 |
| 10-07 13:03 | +5 | DOGE | UP | 0.59 | 0.64 | 0.16 |
| 10-07 13:03 | +10 stop | XRP | UP | 0.54 | 0.66 | 0.86 |
| 10-07 13:03 | +15 | XRP | UP | 0.54 | open |  |
| 10-07 13:03 | +10 | XRP | UP | 0.53 | 0.66 | 0.96 |
| 10-07 13:03 | +5 | XRP | UP | 0.53 | 0.66 | 0.96 |
| 10-07 13:02 | +10 stop | DOGE | DOWN | 0.47 | 0.63 | 1.25 |
| 10-07 13:02 | +10 stop | HYPE | DOWN | 0.37 | 0.63 | 2.23 |
| 10-07 13:02 | +5 | DOGE | DOWN | 0.43 | 0.63 | 1.65 |
