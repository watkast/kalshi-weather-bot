# Range-Scalp Bot

*Updated Thu Nov 19 15:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65093 | 56814 | 8279 (124) | 0 | $-17474.14 | -4.3% |
| **+10¢** | 48623 | 38939 | 9684 (165) | 0 | $-16255.03 | -5.3% |
| **+15¢** | 40767 | 30320 | 10447 (210) | 0 | $-14679.08 | -5.7% |
| **+20¢** | 36308 | 25336 | 10972 (265) | 0 | $-12973.94 | -5.7% |
| **+10¢ (15¢ stop)** | 79219 | 79055 | 164 (98) | 0 | $-29097.23 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 15:17 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 11-19 15:16 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-19 15:16 | +20 | HYPE | DOWN | 0.69 | 0.91 | 2.02 |
| 11-19 15:16 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-19 15:16 | +10 | HYPE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-19 15:16 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-19 15:16 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 11-19 15:16 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 11-19 15:16 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-19 15:16 | +10 | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 11-19 15:16 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 11-19 15:13 | +10 stop | HYPE | DOWN | 0.70 | 0.99 | 2.68 |
| 11-19 15:13 | +20 | HYPE | DOWN | 0.70 | 0.99 | 2.68 |
| 11-19 15:13 | +15 | HYPE | DOWN | 0.70 | 0.99 | 2.68 |
| 11-19 15:13 | +10 | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-19 15:13 | +5 | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-19 15:12 | +10 stop | BTC | UP | 0.70 | 0.84 | 1.15 |
| 11-19 15:12 | +20 | BTC | UP | 0.71 | 0.97 | 2.39 |
| 11-19 15:12 | +15 | BTC | UP | 0.71 | 0.97 | 2.39 |
| 11-19 15:12 | +10 | BTC | UP | 0.71 | 0.84 | 1.05 |
| 11-19 15:12 | +5 | BTC | UP | 0.70 | 0.84 | 1.15 |
| 11-19 15:11 | +5 | BTC | UP | 0.70 | 0.83 | 1.05 |
| 11-19 15:06 | +10 stop | NEAR | UP | 0.69 | 0.85 | 1.36 |
| 11-19 15:06 | +20 | NEAR | UP | 0.69 | no | -7.05 |
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
