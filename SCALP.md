# Range-Scalp Bot

*Updated Sat Nov 21 14:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67421 | 58838 | 8583 (134) | 0 | $-18100.10 | -4.3% |
| **+10¢** | 50355 | 40327 | 10028 (175) | 0 | $-16807.84 | -5.3% |
| **+15¢** | 42236 | 31427 | 10809 (225) | 0 | $-15039.60 | -5.7% |
| **+20¢** | 37593 | 26235 | 11358 (283) | 0 | $-13355.33 | -5.7% |
| **+10¢ (15¢ stop)** | 82078 | 81907 | 171 (105) | 0 | $-30122.57 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 14:08 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 11-21 14:07 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-21 14:07 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-21 14:07 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-21 14:07 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-21 14:07 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.42 |
| 11-21 14:07 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 11-21 14:07 | +5 | BNB | UP | 0.60 | no | -6.16 |
| 11-21 14:06 | +5 | HYPE | UP | 0.51 | 0.57 | 0.24 |
| 11-21 14:06 | +10 stop | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-21 14:06 | +20 | NEAR | DOWN | 0.69 | 0.89 | 1.78 |
| 11-21 14:06 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-21 14:06 | +10 | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-21 14:06 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.62 |
| 11-21 14:06 | +10 stop | HYPE | UP | 0.61 | 0.46 | -1.85 |
| 11-21 14:05 | +10 stop | SOL | DOWN | 0.56 | 0.74 | 1.48 |
| 11-21 14:05 | +15 | XRP | DOWN | 0.65 | 0.84 | 1.67 |
| 11-21 14:05 | +5 | XRP | DOWN | 0.65 | 0.76 | 0.85 |
| 11-21 14:05 | +5 | SOL | DOWN | 0.51 | 0.63 | 0.87 |
| 11-21 14:05 | +10 stop | ZEC | DOWN | 0.55 | 0.72 | 1.37 |
| 11-21 14:05 | +10 stop | XRP | DOWN | 0.59 | 0.76 | 1.40 |
| 11-21 14:05 | +10 stop | BTC | UP | 0.59 | 0.40 | -2.24 |
| 11-21 14:05 | +15 | BTC | UP | 0.59 | no | -6.07 |
| 11-21 14:05 | +10 | BTC | UP | 0.59 | no | -6.07 |
| 11-21 14:05 | +5 | BTC | UP | 0.59 | no | -6.07 |
| 11-21 14:05 | +10 stop | ETH | UP | 0.67 | 0.49 | -2.14 |
| 11-21 14:05 | +10 | ETH | UP | 0.66 | no | -6.76 |
| 11-21 14:05 | +5 | ETH | UP | 0.67 | no | -6.86 |
| 11-21 14:04 | +10 stop | BNB | UP | 0.62 | 0.44 | -2.15 |
| 11-21 14:04 | +15 | BNB | UP | 0.60 | no | -6.17 |
| 11-21 14:04 | +10 | BNB | UP | 0.60 | no | -6.17 |
| 11-21 14:04 | +5 | BNB | UP | 0.60 | 0.67 | 0.37 |
| 11-21 14:04 | +10 stop | DOGE | UP | 0.56 | 0.38 | -2.15 |
| 11-21 14:04 | +15 | DOGE | UP | 0.56 | no | -5.78 |
| 11-21 14:04 | +10 | DOGE | UP | 0.56 | no | -5.78 |
| 11-21 14:04 | +5 | DOGE | UP | 0.56 | 0.64 | 0.45 |
| 11-21 14:04 | +5 | HYPE | UP | 0.59 | 0.67 | 0.46 |
| 11-21 14:04 | +10 stop | SOL | UP | 0.58 | 0.36 | -2.55 |
| 11-21 14:04 | +10 | SOL | UP | 0.59 | no | -6.07 |
| 11-21 14:04 | +5 | SOL | UP | 0.58 | 0.65 | 0.36 |
