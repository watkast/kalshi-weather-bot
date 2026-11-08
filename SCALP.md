# Range-Scalp Bot

*Updated Sun Nov 08 04:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51971 | 45315 | 6656 (80) | 0 | $-14414.66 | -4.4% |
| **+10¢** | 38788 | 31023 | 7765 (106) | 0 | $-13451.58 | -5.5% |
| **+15¢** | 32481 | 24114 | 8367 (135) | 0 | $-12335.75 | -6.1% |
| **+20¢** | 28894 | 20123 | 8771 (180) | 0 | $-10868.21 | -6.0% |
| **+10¢ (15¢ stop)** | 63278 | 63175 | 103 (61) | 0 | $-23409.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 04:12 | +10 stop | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-08 04:12 | +10 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-08 04:12 | +5 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-08 04:11 | +10 stop | SOL | DOWN | 0.52 | 0.76 | 2.09 |
| 11-08 04:11 | +10 stop | ETH | DOWN | 0.57 | 0.71 | 1.07 |
| 11-08 04:11 | +10 stop | HYPE | DOWN | 0.61 | 0.77 | 1.31 |
| 11-08 04:11 | +5 | HYPE | DOWN | 0.61 | 0.77 | 1.31 |
| 11-08 04:09 | +10 stop | ETH | UP | 0.64 | 0.40 | -2.74 |
| 11-08 04:08 | +5 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 11-08 04:08 | +10 stop | XRP | UP | 0.69 | 0.49 | -2.33 |
| 11-08 04:08 | +20 | XRP | UP | 0.69 | no | -7.05 |
| 11-08 04:08 | +15 | XRP | UP | 0.69 | no | -7.05 |
| 11-08 04:08 | +10 | XRP | UP | 0.69 | no | -7.05 |
| 11-08 04:08 | +5 | XRP | UP | 0.69 | 0.75 | 0.31 |
| 11-08 04:07 | +10 stop | SOL | UP | 0.59 | 0.37 | -2.54 |
| 11-08 04:07 | +15 | SOL | UP | 0.59 | no | -6.07 |
| 11-08 04:07 | +10 | SOL | UP | 0.59 | no | -6.07 |
| 11-08 04:07 | +5 | SOL | UP | 0.59 | no | -6.07 |
| 11-08 04:07 | +10 stop | HYPE | UP | 0.52 | 0.34 | -2.14 |
| 11-08 04:07 | +10 | HYPE | UP | 0.52 | no | -5.38 |
| 11-08 04:07 | +5 | HYPE | UP | 0.52 | 0.61 | 0.55 |
| 11-08 04:07 | +10 stop | ETH | UP | 0.65 | 0.48 | -2.04 |
| 11-08 04:07 | +15 | ETH | UP | 0.65 | no | -6.66 |
| 11-08 04:07 | +10 | ETH | UP | 0.65 | no | -6.66 |
| 11-08 04:07 | +5 | ETH | UP | 0.65 | no | -6.66 |
| 11-08 04:07 | +10 stop | BTC | UP | 0.49 | 0.63 | 1.05 |
| 11-08 04:07 | +10 | BTC | UP | 0.49 | 0.63 | 1.05 |
| 11-08 04:07 | +5 | BTC | UP | 0.49 | 0.63 | 1.05 |
| 11-08 04:07 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-08 04:07 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-08 04:07 | +5 | ZEC | UP | 0.68 | 0.75 | 0.40 |
| 11-08 04:05 | +10 stop | NEAR | UP | 0.68 | 0.52 | -1.94 |
| 11-08 04:05 | +10 stop | BNB | UP | 0.71 | 0.81 | 0.74 |
| 11-08 04:05 | +20 | BNB | UP | 0.71 | 0.92 | 1.86 |
| 11-08 04:05 | +15 | BNB | UP | 0.71 | 0.88 | 1.47 |
| 11-08 04:05 | +10 | BNB | UP | 0.71 | 0.81 | 0.74 |
| 11-08 04:05 | +5 | BNB | UP | 0.71 | 0.81 | 0.74 |
| 11-08 04:04 | +5 | HYPE | UP | 0.62 | 0.72 | 0.68 |
| 11-08 04:04 | +5 | ETH | UP | 0.64 | 0.78 | 1.10 |
| 11-08 04:03 | +10 stop | SOL | UP | 0.57 | 0.77 | 1.69 |
