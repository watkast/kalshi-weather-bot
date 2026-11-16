# Range-Scalp Bot

*Updated Mon Nov 16 09:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61802 | 53920 | 7882 (115) | 0 | $-16705.61 | -4.3% |
| **+10¢** | 46170 | 36939 | 9231 (157) | 0 | $-15610.53 | -5.4% |
| **+15¢** | 38693 | 28736 | 9957 (196) | 0 | $-14232.30 | -5.9% |
| **+20¢** | 34495 | 24053 | 10442 (249) | 1 | $-12438.73 | -5.7% |
| **+10¢ (15¢ stop)** | 75220 | 75066 | 154 (90) | 0 | $-27710.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 09:07 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-16 09:07 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-16 09:05 | +10 stop | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-16 09:05 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 11-16 09:05 | +10 | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 11-16 09:05 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 11-16 09:05 | +10 stop | SOL | DOWN | 0.71 | 0.55 | -1.93 |
| 11-16 09:04 | +10 stop | BTC | DOWN | 0.63 | 0.48 | -1.85 |
| 11-16 09:04 | +20 | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-16 09:04 | +15 | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-16 09:04 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-16 09:04 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-16 09:02 | +10 stop | HYPE | DOWN | 0.67 | 0.49 | -2.14 |
| 11-16 09:02 | +20 | HYPE | DOWN | 0.68 | open |  |
| 11-16 09:02 | +15 | HYPE | DOWN | 0.69 | 0.87 | 1.57 |
| 11-16 09:02 | +10 | HYPE | DOWN | 0.68 | 0.82 | 1.13 |
| 11-16 09:02 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 11-16 09:02 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 09:02 | +20 | ZEC | DOWN | 0.65 | 0.88 | 2.06 |
| 11-16 09:02 | +15 | ZEC | DOWN | 0.65 | 0.82 | 1.43 |
| 11-16 09:02 | +10 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 09:02 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-16 09:01 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 09:01 | +20 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 11-16 09:01 | +15 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 11-16 09:01 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 09:01 | +5 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-16 09:01 | +10 stop | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-16 09:01 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-16 09:01 | +15 | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-16 09:01 | +10 | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 11-16 09:01 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 11-16 08:57 | +10 stop | HYPE | DOWN | 0.61 | 0.41 | -2.34 |
| 11-16 08:57 | +20 | HYPE | DOWN | 0.61 | yes | -6.27 |
| 11-16 08:57 | +15 | HYPE | DOWN | 0.63 | yes | -6.47 |
| 11-16 08:57 | +10 | HYPE | DOWN | 0.62 | yes | -6.37 |
| 11-16 08:57 | +5 | HYPE | DOWN | 0.62 | yes | -6.37 |
| 11-16 08:53 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.71 |
| 11-16 08:52 | +10 stop | DOGE | DOWN | 0.62 | 0.80 | 1.51 |
| 11-16 08:52 | +10 stop | NEAR | UP | 0.66 | 0.37 | -3.23 |
