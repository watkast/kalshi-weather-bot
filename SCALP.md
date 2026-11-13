# Range-Scalp Bot

*Updated Fri Nov 13 20:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58631 | 51160 | 7471 (105) | 2 | $-15808.21 | -4.3% |
| **+10¢** | 43796 | 35058 | 8738 (139) | 3 | $-14781.73 | -5.4% |
| **+15¢** | 36702 | 27291 | 9411 (174) | 5 | $-13362.22 | -5.8% |
| **+20¢** | 32696 | 22816 | 9880 (225) | 5 | $-11750.90 | -5.7% |
| **+10¢ (15¢ stop)** | 71398 | 71264 | 134 (82) | 1 | $-26280.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 20:42 | +10 stop | HYPE | UP | 0.60 | open |  |
| 11-13 20:40 | +10 stop | HYPE | UP | 0.63 | 0.43 | -2.35 |
| 11-13 20:40 | +20 | HYPE | UP | 0.63 | open |  |
| 11-13 20:40 | +15 | HYPE | UP | 0.63 | open |  |
| 11-13 20:40 | +10 | HYPE | UP | 0.63 | open |  |
| 11-13 20:40 | +5 | HYPE | UP | 0.63 | open |  |
| 11-13 20:40 | +10 stop | NEAR | DOWN | 0.61 | 0.34 | -3.03 |
| 11-13 20:40 | +10 | NEAR | DOWN | 0.60 | open |  |
| 11-13 20:40 | +5 | NEAR | DOWN | 0.60 | 0.67 | 0.37 |
| 11-13 20:39 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 20:38 | +10 stop | BTC | UP | 0.53 | 0.31 | -2.53 |
| 11-13 20:37 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 11-13 20:37 | +5 | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 11-13 20:37 | +10 stop | HYPE | DOWN | 0.57 | 0.69 | 0.82 |
| 11-13 20:36 | +10 stop | BTC | UP | 0.63 | 0.42 | -2.45 |
| 11-13 20:36 | +15 | BTC | UP | 0.63 | open |  |
| 11-13 20:36 | +10 | BTC | UP | 0.63 | open |  |
| 11-13 20:36 | +5 | BTC | UP | 0.63 | open |  |
| 11-13 20:35 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 11-13 20:35 | +10 | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 11-13 20:35 | +5 | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 11-13 20:35 | +10 stop | NEAR | DOWN | 0.50 | 0.61 | 0.75 |
| 11-13 20:35 | +5 | NEAR | DOWN | 0.50 | 0.61 | 0.75 |
| 11-13 20:34 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 11-13 20:34 | +10 stop | HYPE | DOWN | 0.71 | 0.51 | -2.33 |
| 11-13 20:34 | +10 stop | BTC | DOWN | 0.56 | 0.32 | -2.74 |
| 11-13 20:34 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 11-13 20:33 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-13 20:33 | +10 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-13 20:33 | +5 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-13 20:33 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 11-13 20:33 | +10 stop | BTC | UP | 0.54 | 0.38 | -1.95 |
| 11-13 20:33 | +10 | BTC | UP | 0.55 | 0.67 | 0.86 |
| 11-13 20:33 | +5 | BTC | UP | 0.55 | 0.67 | 0.86 |
| 11-13 20:32 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-13 20:32 | +20 | SOL | DOWN | 0.71 | 0.94 | 2.09 |
| 11-13 20:32 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 11-13 20:32 | +10 | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-13 20:32 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 11-13 20:32 | +10 stop | HYPE | DOWN | 0.67 | 0.46 | -2.45 |
