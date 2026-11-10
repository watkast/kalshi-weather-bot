# Range-Scalp Bot

*Updated Tue Nov 10 01:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54132 | 47223 | 6909 (89) | 1 | $-14723.85 | -4.3% |
| **+10¢** | 40437 | 32374 | 8063 (117) | 1 | $-13683.52 | -5.4% |
| **+15¢** | 33892 | 25202 | 8690 (149) | 1 | $-12444.70 | -5.9% |
| **+20¢** | 30178 | 21064 | 9114 (195) | 0 | $-10860.98 | -5.7% |
| **+10¢ (15¢ stop)** | 65949 | 65839 | 110 (66) | 0 | $-24421.65 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 01:40 | +10 stop | DOGE | UP | 0.70 | 0.38 | -3.52 |
| 11-10 01:40 | +15 | DOGE | UP | 0.70 | open |  |
| 11-10 01:40 | +10 | DOGE | UP | 0.70 | open |  |
| 11-10 01:40 | +5 | DOGE | UP | 0.70 | open |  |
| 11-10 01:40 | +10 stop | NEAR | DOWN | 0.71 | 0.94 | 2.05 |
| 11-10 01:40 | +15 | NEAR | DOWN | 0.71 | 0.94 | 2.05 |
| 11-10 01:40 | +10 | NEAR | DOWN | 0.71 | 0.94 | 2.05 |
| 11-10 01:40 | +5 | NEAR | DOWN | 0.71 | 0.94 | 2.05 |
| 11-10 01:36 | +5 | DOGE | DOWN | 0.61 | 0.77 | 1.28 |
| 11-10 01:36 | +10 stop | NEAR | DOWN | 0.66 | 0.86 | 1.75 |
| 11-10 01:36 | +10 | NEAR | DOWN | 0.66 | 0.86 | 1.75 |
| 11-10 01:36 | +5 | NEAR | DOWN | 0.66 | 0.86 | 1.75 |
| 11-10 01:34 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-10 01:34 | +20 | NEAR | DOWN | 0.70 | 0.94 | 2.15 |
| 11-10 01:34 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-10 01:34 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-10 01:34 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-10 01:32 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-10 01:32 | +20 | DOGE | DOWN | 0.65 | 0.94 | 2.73 |
| 11-10 01:32 | +15 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-10 01:32 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-10 01:32 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-10 01:28 | +10 stop | ZEC | DOWN | 0.64 | 0.83 | 1.63 |
| 11-10 01:27 | +10 stop | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-10 01:27 | +10 stop | NEAR | UP | 0.57 | 0.27 | -3.32 |
| 11-10 01:26 | +10 stop | ZEC | UP | 0.62 | 0.39 | -2.64 |
| 11-10 01:25 | +10 stop | NEAR | UP | 0.71 | 0.55 | -1.93 |
| 11-10 01:25 | +10 stop | HYPE | UP | 0.67 | 0.33 | -3.72 |
| 11-10 01:25 | +10 stop | ZEC | UP | 0.64 | 0.48 | -1.95 |
| 11-10 01:24 | +10 stop | XRP | UP | 0.57 | 0.72 | 1.17 |
| 11-10 01:24 | +10 stop | NEAR | DOWN | 0.51 | 0.35 | -1.94 |
| 11-10 01:24 | +10 | NEAR | DOWN | 0.51 | 0.71 | 1.67 |
| 11-10 01:24 | +10 stop | HYPE | DOWN | 0.55 | 0.35 | -2.34 |
| 11-10 01:24 | +10 stop | ZEC | DOWN | 0.70 | 0.50 | -2.33 |
| 11-10 01:24 | +10 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-10 01:24 | +5 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-10 01:23 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-10 01:22 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-10 01:22 | +20 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-10 01:22 | +15 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
