# Range-Scalp Bot

*Updated Thu Nov 05 07:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48236 | 42019 | 6217 (73) | 1 | $-13808.16 | -4.5% |
| **+10¢** | 36021 | 28798 | 7223 (99) | 1 | $-12664.24 | -5.6% |
| **+15¢** | 30186 | 22409 | 7777 (127) | 1 | $-11563.52 | -6.1% |
| **+20¢** | 26815 | 18668 | 8147 (166) | 1 | $-10218.37 | -6.1% |
| **+10¢ (15¢ stop)** | 58765 | 58672 | 93 (56) | 1 | $-21812.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 07:41 | +10 stop | NEAR | UP | 0.58 | open |  |
| 11-05 07:41 | +5 | NEAR | UP | 0.58 | open |  |
| 11-05 07:40 | +10 stop | NEAR | DOWN | 0.58 | 0.41 | -2.05 |
| 11-05 07:40 | +15 | NEAR | DOWN | 0.58 | open |  |
| 11-05 07:40 | +10 | NEAR | DOWN | 0.58 | open |  |
| 11-05 07:40 | +5 | NEAR | DOWN | 0.58 | 0.64 | 0.25 |
| 11-05 07:38 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 11-05 07:38 | +10 | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 11-05 07:38 | +5 | NEAR | DOWN | 0.58 | 0.70 | 0.85 |
| 11-05 07:38 | +10 stop | NEAR | DOWN | 0.52 | 0.66 | 1.06 |
| 11-05 07:38 | +20 | NEAR | DOWN | 0.52 | open |  |
| 11-05 07:38 | +15 | NEAR | DOWN | 0.52 | 0.70 | 1.47 |
| 11-05 07:38 | +10 | NEAR | DOWN | 0.52 | 0.66 | 1.06 |
| 11-05 07:38 | +5 | NEAR | DOWN | 0.52 | 0.66 | 1.06 |
| 11-05 07:30 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-05 07:30 | +20 | BNB | DOWN | 0.69 | 0.90 | 1.88 |
| 11-05 07:30 | +15 | BNB | DOWN | 0.69 | 0.86 | 1.46 |
| 11-05 07:30 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-05 07:30 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-05 07:27 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-05 07:26 | +10 stop | DOGE | UP | 0.68 | 0.88 | 1.76 |
| 11-05 07:26 | +10 | DOGE | UP | 0.68 | 0.88 | 1.76 |
| 11-05 07:26 | +5 | DOGE | UP | 0.68 | 0.74 | 0.30 |
| 11-05 07:26 | +10 stop | NEAR | UP | 0.64 | 0.86 | 1.94 |
| 11-05 07:26 | +10 | NEAR | UP | 0.64 | 0.86 | 1.94 |
| 11-05 07:26 | +5 | NEAR | UP | 0.64 | 0.72 | 0.48 |
| 11-05 07:25 | +10 stop | DOGE | DOWN | 0.44 | 0.59 | 1.15 |
| 11-05 07:25 | +10 | DOGE | DOWN | 0.44 | 0.59 | 1.15 |
| 11-05 07:25 | +5 | DOGE | DOWN | 0.44 | 0.59 | 1.15 |
| 11-05 07:25 | +10 stop | ZEC | UP | 0.70 | 0.50 | -2.33 |
| 11-05 07:25 | +15 | ZEC | UP | 0.70 | 0.87 | 1.47 |
| 11-05 07:25 | +10 | ZEC | UP | 0.71 | 0.84 | 1.05 |
| 11-05 07:25 | +5 | ZEC | UP | 0.71 | 0.84 | 1.05 |
| 11-05 07:25 | +10 stop | HYPE | UP | 0.53 | 0.72 | 1.57 |
| 11-05 07:25 | +5 | HYPE | UP | 0.53 | 0.72 | 1.57 |
| 11-05 07:25 | +10 stop | NEAR | UP | 0.48 | 0.62 | 1.05 |
| 11-05 07:25 | +15 | NEAR | UP | 0.48 | 0.72 | 2.07 |
| 11-05 07:25 | +10 | NEAR | UP | 0.48 | 0.62 | 1.05 |
| 11-05 07:25 | +5 | NEAR | UP | 0.48 | 0.62 | 1.05 |
| 11-05 07:25 | +10 stop | DOGE | UP | 0.38 | 0.57 | 1.54 |
