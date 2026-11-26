# Range-Scalp Bot

*Updated Thu Nov 26 09:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72483 | 63278 | 9205 (158) | 0 | $-19208.16 | -4.2% |
| **+10¢** | 54060 | 43310 | 10750 (203) | 0 | $-17786.70 | -5.2% |
| **+15¢** | 45269 | 33689 | 11580 (261) | 0 | $-15864.72 | -5.6% |
| **+20¢** | 40294 | 28098 | 12196 (327) | 0 | $-14263.72 | -5.6% |
| **+10¢ (15¢ stop)** | 88251 | 88042 | 209 (128) | 0 | $-32375.45 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 06:14 | +5 | NEAR | DOWN | 0.40 | 0.54 | 1.05 |
| 11-26 06:12 | +10 stop | NEAR | DOWN | 0.66 | 0.45 | -2.43 |
| 11-26 06:12 | +20 | NEAR | DOWN | 0.63 | yes | -6.47 |
| 11-26 06:12 | +15 | NEAR | DOWN | 0.63 | yes | -6.47 |
| 11-26 06:12 | +10 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-26 06:12 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 11-26 06:10 | +5 | NEAR | DOWN | 0.58 | 0.69 | 0.77 |
| 11-26 06:08 | +10 stop | NEAR | DOWN | 0.69 | 0.88 | 1.68 |
| 11-26 06:08 | +20 | NEAR | DOWN | 0.68 | 0.88 | 1.76 |
| 11-26 06:08 | +15 | NEAR | DOWN | 0.68 | 0.88 | 1.76 |
| 11-26 06:08 | +10 | NEAR | DOWN | 0.67 | 0.88 | 1.86 |
| 11-26 06:08 | +5 | NEAR | DOWN | 0.67 | 0.75 | 0.50 |
| 11-26 06:08 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 11-26 06:08 | +10 stop | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-26 06:08 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-26 06:08 | +15 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-26 06:08 | +10 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-26 06:08 | +5 | SOL | DOWN | 0.59 | 0.66 | 0.37 |
| 11-26 05:57 | +10 stop | XRP | DOWN | 0.64 | 0.78 | 1.08 |
| 11-26 05:57 | +20 | XRP | DOWN | 0.64 | 0.99 | 3.30 |
| 11-26 05:57 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.22 |
| 11-26 05:57 | +10 | XRP | DOWN | 0.61 | 0.78 | 1.40 |
| 11-26 05:57 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.18 |
| 11-26 05:53 | +5 | HYPE | DOWN | 0.70 | 0.82 | 0.92 |
| 11-26 05:52 | +10 stop | ZEC | UP | 0.51 | 0.36 | -1.85 |
| 11-26 05:52 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-26 05:52 | +20 | DOGE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-26 05:52 | +15 | DOGE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-26 05:52 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-26 05:52 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-26 05:52 | +5 | ZEC | UP | 0.56 | 0.62 | 0.20 |
| 11-26 05:52 | +10 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 11-26 05:52 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.66 |
| 11-26 05:52 | +10 stop | HYPE | DOWN | 0.55 | 0.68 | 0.94 |
| 11-26 05:52 | +10 | HYPE | DOWN | 0.55 | 0.68 | 1.01 |
| 11-26 05:52 | +5 | HYPE | DOWN | 0.54 | 0.60 | 0.22 |
| 11-26 05:51 | +10 | XRP | DOWN | 0.57 | 0.69 | 0.87 |
| 11-26 05:51 | +5 | XRP | DOWN | 0.57 | 0.64 | 0.35 |
| 11-26 05:51 | +10 stop | ZEC | DOWN | 0.53 | 0.36 | -2.05 |
| 11-26 05:51 | +5 | ZEC | DOWN | 0.52 | 0.58 | 0.24 |
