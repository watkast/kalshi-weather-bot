# Range-Scalp Bot

*Updated Tue Oct 27 10:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36444 | 31820 | 4624 (43) | 1 | $-10106.15 | -4.4% |
| **+10¢** | 27233 | 21886 | 5347 (65) | 1 | $-8918.51 | -5.2% |
| **+15¢** | 22782 | 17043 | 5739 (89) | 3 | $-7860.23 | -5.5% |
| **+20¢** | 20182 | 14170 | 6012 (113) | 6 | $-6899.99 | -5.4% |
| **+10¢ (15¢ stop)** | 44672 | 44609 | 63 (33) | 0 | $-17053.29 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 10:37 | +10 stop | HYPE | UP | 0.53 | 0.35 | -2.14 |
| 10-27 10:37 | +15 | HYPE | UP | 0.56 | open |  |
| 10-27 10:37 | +10 | HYPE | UP | 0.56 | open |  |
| 10-27 10:37 | +5 | HYPE | UP | 0.56 | open |  |
| 10-27 10:36 | +10 stop | NEAR | DOWN | 0.53 | 0.28 | -2.83 |
| 10-27 10:36 | +10 stop | SOL | UP | 0.48 | 0.85 | 3.43 |
| 10-27 10:36 | +15 | SOL | UP | 0.48 | 0.85 | 3.43 |
| 10-27 10:36 | +10 | SOL | UP | 0.48 | 0.85 | 3.43 |
| 10-27 10:36 | +5 | SOL | UP | 0.49 | 0.56 | 0.34 |
| 10-27 10:35 | +10 stop | DOGE | UP | 0.53 | 0.79 | 2.30 |
| 10-27 10:35 | +15 | DOGE | UP | 0.55 | 0.79 | 2.10 |
| 10-27 10:35 | +10 | DOGE | UP | 0.58 | 0.79 | 1.80 |
| 10-27 10:35 | +5 | DOGE | UP | 0.58 | 0.79 | 1.80 |
| 10-27 10:35 | +5 | NEAR | UP | 0.62 | 0.71 | 0.58 |
| 10-27 10:35 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 10-27 10:34 | +10 stop | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-27 10:34 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 10-27 10:32 | +10 stop | HYPE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-27 10:32 | +5 | DOGE | UP | 0.68 | 0.77 | 0.61 |
| 10-27 10:32 | +10 stop | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-27 10:32 | +20 | ZEC | UP | 0.64 | open |  |
| 10-27 10:32 | +15 | ZEC | UP | 0.64 | open |  |
| 10-27 10:32 | +10 | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 10-27 10:32 | +5 | ZEC | UP | 0.63 | 0.69 | 0.28 |
| 10-27 10:31 | +10 stop | BTC | UP | 0.65 | 0.48 | -2.04 |
| 10-27 10:31 | +20 | BTC | UP | 0.65 | open |  |
| 10-27 10:31 | +15 | BTC | UP | 0.65 | open |  |
| 10-27 10:31 | +10 | BTC | UP | 0.65 | 0.78 | 1.01 |
| 10-27 10:31 | +5 | BTC | UP | 0.65 | 0.71 | 0.29 |
| 10-27 10:31 | +10 stop | SOL | UP | 0.66 | 0.77 | 0.81 |
| 10-27 10:31 | +20 | SOL | UP | 0.66 | 0.87 | 1.86 |
| 10-27 10:31 | +15 | SOL | UP | 0.66 | 0.82 | 1.33 |
| 10-27 10:31 | +10 | SOL | UP | 0.66 | 0.77 | 0.81 |
| 10-27 10:31 | +5 | SOL | UP | 0.66 | 0.77 | 0.81 |
| 10-27 10:31 | +10 stop | HYPE | DOWN | 0.66 | 0.49 | -2.00 |
| 10-27 10:31 | +20 | HYPE | DOWN | 0.66 | open |  |
| 10-27 10:31 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.45 |
| 10-27 10:31 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.86 |
| 10-27 10:31 | +5 | HYPE | DOWN | 0.67 | 0.78 | 0.86 |
| 10-27 10:31 | +10 stop | ETH | UP | 0.64 | 0.78 | 1.10 |
