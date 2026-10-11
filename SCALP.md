# Range-Scalp Bot

*Updated Sun Oct 11 19:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12395 | 10696 | 1699 (25) | 2 | $-4104.54 | -5.2% |
| **+10¢** | 9415 | 7448 | 1967 (37) | 2 | $-3854.01 | -6.5% |
| **+15¢** | 7929 | 5838 | 2091 (55) | 2 | $-3297.67 | -6.6% |
| **+20¢** | 7067 | 4890 | 2177 (69) | 2 | $-2771.22 | -6.2% |
| **+10¢ (15¢ stop)** | 15279 | 15238 | 41 (25) | 0 | $-6016.87 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 19:42 | +10 stop | HYPE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-11 19:41 | +10 stop | HYPE | UP | 0.44 | 0.54 | 0.64 |
| 10-11 19:39 | +10 | NEAR | DOWN | 0.69 | 0.86 | 1.46 |
| 10-11 19:39 | +5 | NEAR | DOWN | 0.69 | 0.77 | 0.52 |
| 10-11 19:38 | +15 | XRP | UP | 0.67 | 0.86 | 1.65 |
| 10-11 19:38 | +10 stop | HYPE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-11 19:38 | +10 stop | ETH | UP | 0.60 | 0.85 | 2.24 |
| 10-11 19:38 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-11 19:38 | +10 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-11 19:38 | +5 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-11 19:38 | +5 | SOL | UP | 0.69 | 0.81 | 0.94 |
| 10-11 19:38 | +10 stop | DOGE | UP | 0.62 | 0.81 | 1.62 |
| 10-11 19:38 | +10 stop | XRP | UP | 0.50 | 0.64 | 1.05 |
| 10-11 19:38 | +15 | XRP | UP | 0.50 | 0.68 | 1.46 |
| 10-11 19:38 | +10 | XRP | UP | 0.50 | 0.64 | 1.05 |
| 10-11 19:38 | +5 | XRP | UP | 0.50 | 0.64 | 1.05 |
| 10-11 19:37 | +5 | ETH | UP | 0.71 | 0.85 | 1.16 |
| 10-11 19:36 | +10 stop | BNB | UP | 0.57 | 0.40 | -2.05 |
| 10-11 19:35 | +10 stop | DOGE | UP | 0.55 | 0.73 | 1.48 |
| 10-11 19:35 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.94 |
| 10-11 19:35 | +10 stop | SOL | UP | 0.69 | 0.81 | 0.94 |
| 10-11 19:35 | +20 | SOL | UP | 0.69 | 0.90 | 1.89 |
| 10-11 19:35 | +15 | SOL | UP | 0.69 | 0.90 | 1.90 |
| 10-11 19:35 | +10 | SOL | UP | 0.69 | 0.81 | 0.94 |
| 10-11 19:35 | +10 stop | HYPE | UP | 0.69 | 0.47 | -2.53 |
| 10-11 19:35 | +10 | HYPE | UP | 0.69 | open |  |
| 10-11 19:35 | +10 stop | ETH | UP | 0.65 | 0.50 | -1.84 |
| 10-11 19:35 | +10 | ETH | UP | 0.65 | 0.85 | 1.75 |
| 10-11 19:35 | +5 | ETH | UP | 0.65 | 0.71 | 0.29 |
| 10-11 19:33 | +10 stop | BNB | UP | 0.55 | 0.65 | 0.66 |
| 10-11 19:33 | +10 stop | NEAR | UP | 0.58 | 0.43 | -1.86 |
| 10-11 19:32 | +10 stop | DOGE | UP | 0.63 | 0.46 | -2.05 |
| 10-11 19:32 | +5 | HYPE | UP | 0.70 | open |  |
| 10-11 19:32 | +10 stop | XRP | UP | 0.63 | 0.77 | 1.10 |
| 10-11 19:32 | +20 | XRP | UP | 0.63 | 0.86 | 2.04 |
| 10-11 19:32 | +15 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 10-11 19:32 | +10 | XRP | UP | 0.63 | 0.77 | 1.10 |
| 10-11 19:32 | +5 | XRP | UP | 0.63 | 0.71 | 0.48 |
| 10-11 19:32 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 10-11 19:31 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.20 |
