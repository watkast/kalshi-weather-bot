# Range-Scalp Bot

*Updated Thu Nov 19 15:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65087 | 56808 | 8279 (124) | 0 | $-17477.96 | -4.3% |
| **+10¢** | 48619 | 38935 | 9684 (165) | 0 | $-16258.52 | -5.3% |
| **+15¢** | 40763 | 30316 | 10447 (210) | 0 | $-14686.63 | -5.7% |
| **+20¢** | 36303 | 25332 | 10971 (265) | 1 | $-12975.84 | -5.7% |
| **+10¢ (15¢ stop)** | 79215 | 79051 | 164 (98) | 0 | $-29102.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 15:06 | +10 stop | NEAR | UP | 0.69 | 0.85 | 1.36 |
| 11-19 15:06 | +20 | NEAR | UP | 0.69 | open |  |
| 11-19 15:06 | +15 | NEAR | UP | 0.69 | 0.85 | 1.36 |
| 11-19 15:06 | +10 | NEAR | UP | 0.69 | 0.85 | 1.36 |
| 11-19 15:06 | +5 | NEAR | UP | 0.69 | 0.74 | 0.21 |
| 11-19 15:01 | +10 stop | HYPE | UP | 0.63 | 0.74 | 0.79 |
| 11-19 15:00 | +10 stop | HYPE | UP | 0.70 | 0.55 | -1.83 |
| 11-19 15:00 | +20 | HYPE | UP | 0.70 | 0.92 | 2.04 |
| 11-19 15:00 | +15 | HYPE | UP | 0.70 | 0.88 | 1.57 |
| 11-19 15:00 | +10 | HYPE | UP | 0.70 | 0.88 | 1.57 |
| 11-19 15:00 | +5 | HYPE | UP | 0.70 | 0.79 | 0.63 |
| 11-19 14:54 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-19 14:53 | +10 stop | HYPE | UP | 0.59 | 0.44 | -1.85 |
| 11-19 14:53 | +10 | HYPE | UP | 0.59 | no | -6.07 |
| 11-19 14:53 | +5 | HYPE | UP | 0.58 | no | -5.98 |
| 11-19 14:53 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-19 14:53 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-19 14:53 | +5 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-19 14:52 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 14:52 | +10 stop | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 11-19 14:52 | +10 stop | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 11-19 14:51 | +10 stop | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-19 14:51 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 11-19 14:51 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.69 |
| 11-19 14:51 | +10 stop | HYPE | UP | 0.63 | 0.74 | 0.79 |
| 11-19 14:51 | +20 | HYPE | UP | 0.63 | no | -6.47 |
| 11-19 14:51 | +15 | HYPE | UP | 0.63 | no | -6.47 |
| 11-19 14:51 | +10 | HYPE | UP | 0.63 | 0.74 | 0.79 |
| 11-19 14:51 | +5 | HYPE | UP | 0.61 | 0.74 | 0.99 |
| 11-19 14:50 | +10 | DOGE | UP | 0.51 | 0.68 | 1.36 |
| 11-19 14:50 | +5 | DOGE | UP | 0.50 | 0.68 | 1.46 |
| 11-19 14:50 | +5 | BTC | UP | 0.64 | no | -6.57 |
| 11-19 14:50 | +10 | DOGE | UP | 0.51 | 0.61 | 0.65 |
| 11-19 14:50 | +5 | DOGE | UP | 0.51 | 0.61 | 0.65 |
| 11-19 14:50 | +10 stop | XRP | UP | 0.47 | 0.57 | 0.64 |
| 11-19 14:50 | +10 stop | BNB | UP | 0.54 | 0.32 | -2.54 |
| 11-19 14:50 | +10 | BNB | UP | 0.56 | no | -5.78 |
| 11-19 14:50 | +5 | BNB | UP | 0.54 | 0.60 | 0.25 |
| 11-19 14:49 | +10 stop | DOGE | UP | 0.64 | 0.49 | -1.85 |
| 11-19 14:49 | +10 stop | ZEC | UP | 0.66 | 0.49 | -2.04 |
