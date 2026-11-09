# Range-Scalp Bot

*Updated Mon Nov 09 12:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53662 | 46802 | 6860 (86) | 2 | $-14712.67 | -4.4% |
| **+10¢** | 40088 | 32086 | 8002 (112) | 4 | $-13687.35 | -5.4% |
| **+15¢** | 33595 | 24972 | 8623 (143) | 4 | $-12468.71 | -5.9% |
| **+20¢** | 29899 | 20853 | 9046 (189) | 4 | $-10954.56 | -5.8% |
| **+10¢ (15¢ stop)** | 65384 | 65278 | 106 (63) | 4 | $-24200.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 12:46 | +10 stop | DOGE | UP | 0.61 | open |  |
| 11-09 12:46 | +20 | DOGE | UP | 0.61 | open |  |
| 11-09 12:46 | +15 | DOGE | UP | 0.61 | open |  |
| 11-09 12:46 | +10 | DOGE | UP | 0.61 | open |  |
| 11-09 12:46 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 11-09 12:46 | +10 stop | ZEC | UP | 0.53 | open |  |
| 11-09 12:46 | +20 | ZEC | UP | 0.53 | open |  |
| 11-09 12:46 | +15 | ZEC | UP | 0.53 | open |  |
| 11-09 12:46 | +10 | ZEC | UP | 0.53 | open |  |
| 11-09 12:46 | +5 | ZEC | UP | 0.53 | 0.58 | 0.14 |
| 11-09 12:46 | +10 stop | BNB | UP | 0.58 | open |  |
| 11-09 12:46 | +20 | BNB | UP | 0.58 | open |  |
| 11-09 12:46 | +15 | BNB | UP | 0.58 | open |  |
| 11-09 12:46 | +10 | BNB | UP | 0.58 | open |  |
| 11-09 12:46 | +5 | BNB | UP | 0.58 | open |  |
| 11-09 12:46 | +10 stop | HYPE | UP | 0.59 | open |  |
| 11-09 12:46 | +20 | HYPE | UP | 0.59 | open |  |
| 11-09 12:46 | +15 | HYPE | UP | 0.59 | open |  |
| 11-09 12:46 | +10 | HYPE | UP | 0.59 | open |  |
| 11-09 12:46 | +5 | HYPE | UP | 0.58 | open |  |
| 11-09 12:43 | +10 stop | ZEC | UP | 0.41 | 0.60 | 1.56 |
| 11-09 12:43 | +10 stop | BNB | UP | 0.30 | 0.64 | 3.08 |
| 11-09 12:42 | +10 stop | ZEC | DOWN | 0.56 | 0.30 | -2.93 |
| 11-09 12:42 | +20 | ZEC | DOWN | 0.56 | 0.83 | 2.42 |
| 11-09 12:42 | +15 | ZEC | DOWN | 0.56 | 0.83 | 2.42 |
| 11-09 12:42 | +10 | ZEC | DOWN | 0.56 | 0.83 | 2.42 |
| 11-09 12:42 | +5 | ZEC | DOWN | 0.56 | 0.83 | 2.42 |
| 11-09 12:41 | +10 stop | SOL | UP | 0.68 | 0.13 | -5.74 |
| 11-09 12:41 | +20 | SOL | UP | 0.68 | no | -6.96 |
| 11-09 12:41 | +15 | SOL | UP | 0.68 | no | -6.96 |
| 11-09 12:41 | +10 | SOL | UP | 0.68 | no | -6.96 |
| 11-09 12:41 | +5 | SOL | UP | 0.68 | no | -6.96 |
| 11-09 12:41 | +10 stop | BNB | DOWN | 0.50 | 0.35 | -1.84 |
| 11-09 12:41 | +20 | BNB | DOWN | 0.50 | 0.92 | 4.01 |
| 11-09 12:41 | +15 | BNB | DOWN | 0.50 | 0.92 | 4.01 |
| 11-09 12:41 | +10 | BNB | DOWN | 0.50 | 0.60 | 0.65 |
| 11-09 12:37 | +5 | SOL | UP | 0.60 | 0.75 | 1.19 |
| 11-09 12:37 | +10 stop | ZEC | DOWN | 0.70 | 0.33 | -4.01 |
| 11-09 12:37 | +10 stop | SOL | UP | 0.54 | 0.75 | 1.78 |
| 11-09 12:37 | +5 | SOL | UP | 0.54 | 0.59 | 0.15 |
