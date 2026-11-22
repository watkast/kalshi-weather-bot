# Range-Scalp Bot

*Updated Sun Nov 22 03:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68188 | 59510 | 8678 (138) | 5 | $-18294.64 | -4.3% |
| **+10¢** | 50915 | 40777 | 10138 (181) | 4 | $-16970.24 | -5.3% |
| **+15¢** | 42677 | 31749 | 10928 (231) | 5 | $-15212.77 | -5.7% |
| **+20¢** | 37992 | 26507 | 11485 (289) | 6 | $-13537.72 | -5.7% |
| **+10¢ (15¢ stop)** | 83039 | 82860 | 179 (111) | 0 | $-30500.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 03:27 | +10 stop | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 11-22 03:26 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 11-22 03:26 | +10 stop | DOGE | UP | 0.53 | 0.64 | 0.75 |
| 11-22 03:25 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-22 03:25 | +10 stop | ETH | UP | 0.40 | 0.55 | 1.15 |
| 11-22 03:25 | +15 | NEAR | UP | 0.51 | 0.72 | 1.73 |
| 11-22 03:25 | +20 | HYPE | UP | 0.46 | open |  |
| 11-22 03:25 | +15 | HYPE | UP | 0.45 | open |  |
| 11-22 03:25 | +10 | HYPE | UP | 0.45 | 0.57 | 0.84 |
| 11-22 03:25 | +5 | HYPE | UP | 0.45 | 0.57 | 0.84 |
| 11-22 03:25 | +10 stop | ZEC | UP | 0.64 | 0.42 | -2.55 |
| 11-22 03:25 | +5 | ZEC | UP | 0.64 | open |  |
| 11-22 03:24 | +10 stop | NEAR | UP | 0.70 | 0.53 | -1.99 |
| 11-22 03:24 | +10 stop | HYPE | UP | 0.71 | 0.49 | -2.53 |
| 11-22 03:24 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 11-22 03:24 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 11-22 03:24 | +10 stop | XRP | UP | 0.69 | 0.83 | 1.15 |
| 11-22 03:23 | +10 stop | NEAR | DOWN | 0.62 | 0.42 | -2.35 |
| 11-22 03:23 | +10 | NEAR | DOWN | 0.62 | open |  |
| 11-22 03:23 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-22 03:23 | +10 stop | ZEC | DOWN | 0.71 | 0.48 | -2.63 |
| 11-22 03:23 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-22 03:23 | +10 stop | DOGE | UP | 0.52 | 0.63 | 0.75 |
| 11-22 03:22 | +10 | XRP | UP | 0.61 | 0.75 | 1.09 |
| 11-22 03:22 | +10 | ZEC | UP | 0.48 | 0.59 | 0.75 |
| 11-22 03:22 | +10 stop | HYPE | UP | 0.56 | 0.27 | -3.22 |
| 11-22 03:22 | +20 | HYPE | UP | 0.56 | 0.76 | 1.69 |
| 11-22 03:22 | +15 | HYPE | UP | 0.55 | 0.76 | 1.79 |
| 11-22 03:22 | +10 | HYPE | UP | 0.55 | 0.66 | 0.76 |
| 11-22 03:22 | +10 stop | ZEC | UP | 0.49 | 0.59 | 0.65 |
| 11-22 03:22 | +10 stop | XRP | UP | 0.66 | 0.46 | -2.34 |
| 11-22 03:22 | +5 | XRP | UP | 0.66 | 0.75 | 0.60 |
| 11-22 03:22 | +10 stop | ETH | UP | 0.67 | 0.50 | -2.04 |
| 11-22 03:20 | +10 stop | BTC | DOWN | 0.56 | 0.32 | -2.74 |
| 11-22 03:20 | +10 stop | DOGE | DOWN | 0.49 | 0.34 | -1.84 |
| 11-22 03:19 | +10 stop | SOL | UP | 0.55 | 0.65 | 0.66 |
| 11-22 03:19 | +10 stop | BNB | DOWN | 0.54 | 0.33 | -2.46 |
| 11-22 03:19 | +10 stop | ZEC | DOWN | 0.66 | 0.47 | -2.24 |
| 11-22 03:18 | +10 stop | NEAR | DOWN | 0.60 | 0.42 | -2.12 |
| 11-22 03:18 | +10 | BTC | UP | 0.55 | 0.67 | 0.86 |
