# Range-Scalp Bot

*Updated Wed Oct 21 16:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27393 | 23847 | 3546 (39) | 0 | $-8021.21 | -4.6% |
| **+10¢** | 20602 | 16506 | 4096 (55) | 0 | $-7094.26 | -5.5% |
| **+15¢** | 17255 | 12848 | 4407 (78) | 0 | $-6336.46 | -5.9% |
| **+20¢** | 15275 | 10657 | 4618 (98) | 0 | $-5692.17 | -5.9% |
| **+10¢ (15¢ stop)** | 33615 | 33556 | 59 (32) | 0 | $-12511.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 15:58 | +10 stop | DOGE | UP | 0.65 | 0.04 | -6.28 |
| 10-21 15:58 | +20 | DOGE | UP | 0.65 | no | -6.66 |
| 10-21 15:58 | +15 | DOGE | UP | 0.65 | no | -6.66 |
| 10-21 15:58 | +10 | DOGE | UP | 0.66 | no | -6.76 |
| 10-21 15:57 | +5 | BNB | UP | 0.68 | no | -6.96 |
| 10-21 15:56 | +10 stop | SOL | DOWN | 0.63 | 0.48 | -1.85 |
| 10-21 15:55 | +20 | DOGE | UP | 0.51 | 0.72 | 1.80 |
| 10-21 15:55 | +15 | DOGE | UP | 0.51 | 0.66 | 1.19 |
| 10-21 15:55 | +10 | DOGE | UP | 0.51 | 0.66 | 1.19 |
| 10-21 15:55 | +20 | BTC | UP | 0.67 | 0.93 | 2.36 |
| 10-21 15:54 | +10 stop | DOGE | UP | 0.70 | 0.42 | -3.13 |
| 10-21 15:54 | +10 | HYPE | UP | 0.66 | 0.83 | 1.44 |
| 10-21 15:54 | +10 stop | BNB | UP | 0.67 | 0.07 | -6.20 |
| 10-21 15:54 | +20 | BNB | UP | 0.67 | no | -6.86 |
| 10-21 15:54 | +15 | BNB | UP | 0.68 | no | -6.96 |
| 10-21 15:54 | +10 | BNB | UP | 0.68 | no | -6.96 |
| 10-21 15:54 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 10-21 15:53 | +10 | DOGE | UP | 0.52 | 0.66 | 1.06 |
| 10-21 15:53 | +5 | HYPE | UP | 0.67 | 0.73 | 0.26 |
| 10-21 15:53 | +10 stop | HYPE | UP | 0.71 | 0.83 | 0.95 |
| 10-21 15:53 | +10 stop | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-21 15:53 | +15 | BTC | UP | 0.61 | 0.84 | 2.03 |
| 10-21 15:53 | +10 | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-21 15:53 | +15 | DOGE | UP | 0.55 | 0.71 | 1.27 |
| 10-21 15:53 | +10 | DOGE | UP | 0.55 | 0.67 | 0.86 |
| 10-21 15:53 | +10 stop | SOL | UP | 0.52 | 0.32 | -2.34 |
| 10-21 15:53 | +5 | DOGE | UP | 0.68 | no | -6.96 |
| 10-21 15:53 | +10 stop | DOGE | UP | 0.69 | 0.53 | -1.93 |
| 10-21 15:52 | +10 stop | SOL | DOWN | 0.63 | 0.36 | -3.04 |
| 10-21 15:52 | +10 stop | ETH | UP | 0.62 | 0.82 | 1.72 |
| 10-21 15:52 | +10 stop | BTC | DOWN | 0.55 | 0.34 | -2.44 |
| 10-21 15:52 | +5 | BTC | DOWN | 0.55 | yes | -5.68 |
| 10-21 15:52 | +10 stop | BNB | DOWN | 0.60 | 0.24 | -3.90 |
| 10-21 15:51 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 10-21 15:51 | +10 stop | ETH | DOWN | 0.62 | 0.42 | -2.35 |
| 10-21 15:49 | +10 stop | NEAR | DOWN | 0.56 | 0.41 | -1.85 |
| 10-21 15:49 | +10 stop | ZEC | DOWN | 0.61 | 0.23 | -4.10 |
| 10-21 15:49 | +10 stop | ETH | UP | 0.71 | 0.51 | -2.33 |
| 10-21 15:49 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 10-21 15:49 | +10 stop | HYPE | DOWN | 0.63 | 0.76 | 1.00 |
