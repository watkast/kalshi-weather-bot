# Range-Scalp Bot

*Updated Wed Oct 21 16:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27464 | 23916 | 3548 (39) | 5 | $-7994.91 | -4.6% |
| **+10¢** | 20645 | 16545 | 4100 (55) | 6 | $-7074.96 | -5.4% |
| **+15¢** | 17290 | 12878 | 4412 (78) | 6 | $-6322.39 | -5.8% |
| **+20¢** | 15304 | 10681 | 4623 (98) | 7 | $-5674.86 | -5.9% |
| **+10¢ (15¢ stop)** | 33685 | 33626 | 59 (32) | 1 | $-12515.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 16:41 | +10 stop | BTC | UP | 0.54 | open |  |
| 10-21 16:40 | +10 stop | ZEC | UP | 0.46 | 0.61 | 1.15 |
| 10-21 16:40 | +20 | ZEC | UP | 0.46 | open |  |
| 10-21 16:40 | +15 | ZEC | UP | 0.46 | 0.61 | 1.15 |
| 10-21 16:40 | +10 | ZEC | UP | 0.49 | 0.61 | 0.85 |
| 10-21 16:40 | +5 | ZEC | UP | 0.51 | 0.61 | 0.70 |
| 10-21 16:40 | +10 stop | SOL | UP | 0.50 | 0.34 | -1.94 |
| 10-21 16:40 | +5 | SOL | UP | 0.50 | 0.58 | 0.44 |
| 10-21 16:38 | +10 stop | DOGE | UP | 0.58 | 0.73 | 1.18 |
| 10-21 16:37 | +10 stop | SOL | DOWN | 0.71 | 0.49 | -2.53 |
| 10-21 16:37 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-21 16:37 | +15 | SOL | DOWN | 0.71 | open |  |
| 10-21 16:37 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-21 16:37 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-21 16:37 | +10 stop | BNB | DOWN | 0.65 | 0.48 | -2.04 |
| 10-21 16:37 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-21 16:37 | +15 | BNB | DOWN | 0.65 | open |  |
| 10-21 16:37 | +10 | BNB | DOWN | 0.65 | open |  |
| 10-21 16:37 | +5 | BNB | DOWN | 0.65 | open |  |
| 10-21 16:37 | +10 stop | ETH | DOWN | 0.60 | 0.40 | -2.34 |
| 10-21 16:37 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-21 16:37 | +15 | ETH | DOWN | 0.60 | open |  |
| 10-21 16:37 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-21 16:37 | +5 | ETH | DOWN | 0.61 | open |  |
| 10-21 16:37 | +10 stop | BTC | DOWN | 0.60 | 0.43 | -2.05 |
| 10-21 16:37 | +15 | BTC | DOWN | 0.60 | open |  |
| 10-21 16:37 | +10 | BTC | DOWN | 0.60 | open |  |
| 10-21 16:37 | +5 | BTC | DOWN | 0.60 | open |  |
| 10-21 16:36 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-21 16:34 | +10 stop | XRP | DOWN | 0.57 | 0.70 | 0.97 |
| 10-21 16:34 | +5 | XRP | DOWN | 0.57 | 0.70 | 0.97 |
| 10-21 16:33 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-21 16:33 | +5 | XRP | DOWN | 0.57 | 0.63 | 0.25 |
| 10-21 16:32 | +10 stop | DOGE | DOWN | 0.66 | 0.40 | -2.93 |
| 10-21 16:32 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-21 16:32 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-21 16:32 | +10 stop | HYPE | UP | 0.53 | 0.75 | 1.84 |
| 10-21 16:32 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-21 16:32 | +10 stop | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-21 16:32 | +10 | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
