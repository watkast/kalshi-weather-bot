# Range-Scalp Bot

*Updated Fri Oct 23 07:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29941 | 26066 | 3875 (39) | 0 | $-8810.71 | -4.7% |
| **+10¢** | 22447 | 17961 | 4486 (55) | 0 | $-7917.01 | -5.6% |
| **+15¢** | 18796 | 13974 | 4822 (78) | 0 | $-7132.72 | -6.0% |
| **+20¢** | 16638 | 11587 | 5051 (101) | 0 | $-6434.34 | -6.2% |
| **+10¢ (15¢ stop)** | 36738 | 36679 | 59 (32) | 0 | $-13841.01 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 07:13 | +10 stop | HYPE | DOWN | 0.57 | 0.34 | -2.64 |
| 10-23 07:13 | +5 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 10-23 07:12 | +10 stop | HYPE | UP | 0.71 | 0.47 | -2.73 |
| 10-23 07:11 | +10 stop | BNB | DOWN | 0.63 | 0.91 | 2.58 |
| 10-23 07:11 | +20 | BNB | DOWN | 0.63 | 0.91 | 2.58 |
| 10-23 07:11 | +15 | BNB | DOWN | 0.63 | 0.91 | 2.58 |
| 10-23 07:11 | +10 | BNB | DOWN | 0.63 | 0.91 | 2.58 |
| 10-23 07:11 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 10-23 07:06 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 10-23 07:06 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 10-23 07:06 | +20 | BNB | DOWN | 0.59 | 0.81 | 1.92 |
| 10-23 07:06 | +15 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 10-23 07:06 | +10 | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 10-23 07:06 | +5 | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 10-23 07:06 | +10 stop | HYPE | DOWN | 0.55 | 0.73 | 1.48 |
| 10-23 07:06 | +10 stop | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 10-23 07:06 | +10 | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 10-23 07:06 | +5 | XRP | DOWN | 0.57 | 0.65 | 0.46 |
| 10-23 07:05 | +10 stop | NEAR | DOWN | 0.64 | 0.48 | -1.95 |
| 10-23 07:05 | +10 stop | ZEC | DOWN | 0.67 | 0.51 | -1.94 |
| 10-23 07:05 | +5 | ZEC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-23 07:02 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-23 07:02 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-23 07:02 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-23 07:02 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-23 07:02 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-23 07:02 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 10-23 07:02 | +10 stop | ZEC | UP | 0.56 | 0.41 | -1.85 |
| 10-23 07:02 | +10 | ZEC | UP | 0.56 | no | -5.75 |
| 10-23 07:02 | +5 | ZEC | UP | 0.56 | 0.62 | 0.28 |
| 10-23 07:01 | +10 stop | BNB | UP | 0.47 | 0.26 | -2.42 |
| 10-23 07:01 | +10 stop | XRP | UP | 0.52 | 0.65 | 0.96 |
| 10-23 07:01 | +20 | XRP | UP | 0.52 | no | -5.38 |
| 10-23 07:01 | +15 | XRP | UP | 0.52 | no | -5.38 |
| 10-23 07:01 | +10 | XRP | UP | 0.52 | 0.65 | 0.96 |
| 10-23 07:01 | +5 | XRP | UP | 0.52 | 0.65 | 0.96 |
| 10-23 07:01 | +10 stop | SOL | UP | 0.60 | 0.42 | -2.15 |
| 10-23 07:01 | +20 | SOL | UP | 0.60 | no | -6.17 |
| 10-23 07:01 | +15 | SOL | UP | 0.60 | no | -6.17 |
| 10-23 07:01 | +10 | SOL | UP | 0.60 | no | -6.17 |
