# Range-Scalp Bot

*Updated Wed Nov 18 05:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63688 | 55546 | 8142 (118) | 2 | $-17417.65 | -4.3% |
| **+10¢** | 47580 | 38049 | 9531 (159) | 2 | $-16346.70 | -5.5% |
| **+15¢** | 39897 | 29620 | 10277 (204) | 2 | $-14815.66 | -5.9% |
| **+20¢** | 35535 | 24749 | 10786 (259) | 2 | $-13090.49 | -5.9% |
| **+10¢ (15¢ stop)** | 77493 | 77335 | 158 (93) | 0 | $-28461.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 05:57 | +10 stop | DOGE | DOWN | 0.45 | 0.56 | 0.73 |
| 11-18 05:56 | +10 stop | NEAR | DOWN | 0.68 | 0.52 | -1.94 |
| 11-18 05:56 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-18 05:56 | +5 | DOGE | UP | 0.64 | open |  |
| 11-18 05:54 | +5 | DOGE | UP | 0.56 | 0.68 | 0.86 |
| 11-18 05:54 | +10 stop | NEAR | DOWN | 0.70 | 0.49 | -2.41 |
| 11-18 05:54 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-18 05:54 | +15 | NEAR | DOWN | 0.70 | open |  |
| 11-18 05:54 | +10 | NEAR | DOWN | 0.70 | open |  |
| 11-18 05:54 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.34 |
| 11-18 05:53 | +10 stop | HYPE | DOWN | 0.48 | 0.60 | 0.85 |
| 11-18 05:53 | +10 stop | DOGE | UP | 0.67 | 0.41 | -2.93 |
| 11-18 05:53 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 11-18 05:52 | +10 stop | ZEC | UP | 0.70 | 0.46 | -2.73 |
| 11-18 05:51 | +10 stop | SOL | DOWN | 0.53 | 0.72 | 1.57 |
| 11-18 05:51 | +10 stop | HYPE | DOWN | 0.69 | 0.51 | -2.13 |
| 11-18 05:51 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-18 05:51 | +10 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-18 05:51 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.52 |
| 11-18 05:51 | +5 | DOGE | UP | 0.57 | 0.62 | 0.15 |
| 11-18 05:51 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-18 05:51 | +20 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 11-18 05:51 | +15 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 11-18 05:51 | +10 | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-18 05:51 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-18 05:51 | +5 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-18 05:50 | +10 stop | DOGE | DOWN | 0.50 | 0.33 | -2.04 |
| 11-18 05:50 | +5 | DOGE | DOWN | 0.50 | 0.55 | 0.17 |
| 11-18 05:49 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.15 |
| 11-18 05:49 | +10 stop | DOGE | DOWN | 0.70 | 0.55 | -1.83 |
| 11-18 05:49 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-18 05:48 | +10 stop | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 11-18 05:48 | +10 stop | SOL | DOWN | 0.71 | 0.56 | -1.83 |
| 11-18 05:48 | +15 | SOL | DOWN | 0.71 | 0.92 | 1.85 |
| 11-18 05:48 | +10 | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-18 05:48 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 11-18 05:48 | +5 | BTC | DOWN | 0.66 | 0.75 | 0.60 |
| 11-18 05:48 | +10 stop | DOGE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-18 05:48 | +10 | DOGE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-18 05:47 | +5 | DOGE | DOWN | 0.60 | 0.69 | 0.58 |
