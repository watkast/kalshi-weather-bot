# Range-Scalp Bot

*Updated Sun Oct 25 08:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32833 | 28634 | 4199 (42) | 0 | $-9303.73 | -4.5% |
| **+10¢** | 24581 | 19719 | 4862 (60) | 0 | $-8310.92 | -5.4% |
| **+15¢** | 20574 | 15341 | 5233 (83) | 0 | $-7484.66 | -5.8% |
| **+20¢** | 18229 | 12751 | 5478 (105) | 0 | $-6617.53 | -5.8% |
| **+10¢ (15¢ stop)** | 40313 | 40253 | 60 (32) | 0 | $-15392.26 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 08:11 | +10 stop | XRP | DOWN | 0.71 | 0.35 | -3.91 |
| 10-25 08:11 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 08:11 | +5 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 08:08 | +10 stop | NEAR | DOWN | 0.68 | 0.82 | 1.13 |
| 10-25 08:07 | +20 | XRP | UP | 0.52 | 0.91 | 3.67 |
| 10-25 08:07 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 10-25 08:07 | +5 | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 10-25 08:07 | +10 stop | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 10-25 08:06 | +15 | XRP | UP | 0.70 | 0.91 | 1.90 |
| 10-25 08:06 | +5 | HYPE | UP | 0.62 | no | -6.37 |
| 10-25 08:06 | +10 stop | XRP | UP | 0.68 | 0.39 | -3.23 |
| 10-25 08:05 | +10 stop | HYPE | UP | 0.64 | 0.45 | -2.25 |
| 10-25 08:05 | +10 | HYPE | UP | 0.64 | no | -6.57 |
| 10-25 08:05 | +5 | HYPE | UP | 0.64 | 0.73 | 0.59 |
| 10-25 08:05 | +10 stop | NEAR | UP | 0.64 | 0.37 | -3.04 |
| 10-25 08:05 | +10 stop | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-25 08:05 | +20 | DOGE | DOWN | 0.64 | 0.85 | 1.84 |
| 10-25 08:05 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-25 08:05 | +10 | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-25 08:05 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-25 08:05 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 10-25 08:04 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
| 10-25 08:04 | +10 stop | HYPE | DOWN | 0.43 | 0.62 | 1.51 |
| 10-25 08:04 | +10 | HYPE | DOWN | 0.43 | 0.62 | 1.51 |
| 10-25 08:04 | +5 | HYPE | DOWN | 0.43 | 0.62 | 1.51 |
| 10-25 08:04 | +10 stop | SOL | DOWN | 0.59 | 0.43 | -1.95 |
| 10-25 08:04 | +20 | SOL | DOWN | 0.59 | 0.87 | 2.55 |
| 10-25 08:04 | +15 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-25 08:04 | +10 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-25 08:04 | +5 | SOL | DOWN | 0.59 | 0.67 | 0.47 |
| 10-25 08:04 | +10 stop | BNB | DOWN | 0.58 | 0.78 | 1.69 |
| 10-25 08:04 | +20 | BNB | DOWN | 0.58 | 0.78 | 1.69 |
| 10-25 08:04 | +15 | BNB | DOWN | 0.58 | 0.78 | 1.69 |
| 10-25 08:04 | +10 | BNB | DOWN | 0.58 | 0.78 | 1.69 |
| 10-25 08:04 | +5 | BNB | DOWN | 0.59 | 0.65 | 0.27 |
| 10-25 08:03 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-25 08:03 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-25 08:03 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 10-25 08:03 | +10 stop | NEAR | DOWN | 0.69 | 0.42 | -3.03 |
| 10-25 08:03 | +20 | NEAR | DOWN | 0.69 | 0.90 | 1.88 |
