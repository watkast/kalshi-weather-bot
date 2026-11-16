# Range-Scalp Bot

*Updated Mon Nov 16 00:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61456 | 53627 | 7829 (115) | 0 | $-16535.89 | -4.3% |
| **+10¢** | 45901 | 36727 | 9174 (156) | 0 | $-15511.26 | -5.4% |
| **+15¢** | 38454 | 28556 | 9898 (195) | 0 | $-14159.54 | -5.9% |
| **+20¢** | 34277 | 23894 | 10383 (247) | 0 | $-12420.53 | -5.8% |
| **+10¢ (15¢ stop)** | 74787 | 74633 | 154 (90) | 0 | $-27496.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 00:38 | +10 stop | HYPE | DOWN | 0.47 | 0.59 | 0.85 |
| 11-16 00:36 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-16 00:36 | +10 stop | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 11-16 00:36 | +10 | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 11-16 00:35 | +10 stop | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 11-16 00:35 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-16 00:34 | +10 stop | DOGE | DOWN | 0.59 | 0.77 | 1.50 |
| 11-16 00:34 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-16 00:34 | +10 stop | BTC | UP | 0.53 | 0.34 | -2.24 |
| 11-16 00:34 | +10 stop | BNB | UP | 0.57 | 0.39 | -2.15 |
| 11-16 00:34 | +10 stop | DOGE | DOWN | 0.46 | 0.58 | 0.84 |
| 11-16 00:34 | +10 stop | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
| 11-16 00:33 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 11-16 00:33 | +10 stop | SOL | DOWN | 0.54 | 0.69 | 1.17 |
| 11-16 00:33 | +10 stop | HYPE | UP | 0.54 | 0.35 | -2.24 |
| 11-16 00:32 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 11-16 00:32 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-16 00:32 | +20 | NEAR | DOWN | 0.55 | 0.77 | 1.89 |
| 11-16 00:32 | +15 | NEAR | DOWN | 0.55 | 0.77 | 1.89 |
| 11-16 00:32 | +10 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-16 00:32 | +5 | NEAR | DOWN | 0.55 | 0.61 | 0.25 |
| 11-16 00:32 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-16 00:32 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 00:32 | +5 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 00:31 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-16 00:31 | +10 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-16 00:31 | +10 stop | BNB | DOWN | 0.67 | 0.51 | -1.94 |
| 11-16 00:31 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-16 00:31 | +15 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 11-16 00:31 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-16 00:31 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-16 00:31 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 11-16 00:31 | +20 | ZEC | DOWN | 0.71 | 0.92 | 1.90 |
| 11-16 00:31 | +10 stop | HYPE | DOWN | 0.68 | 0.53 | -1.84 |
| 11-16 00:31 | +20 | HYPE | DOWN | 0.68 | 0.92 | 2.17 |
| 11-16 00:31 | +15 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-16 00:31 | +10 | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-16 00:31 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-16 00:31 | +10 stop | DOGE | DOWN | 0.71 | 0.45 | -2.93 |
| 11-16 00:31 | +20 | DOGE | DOWN | 0.71 | 0.92 | 1.87 |
