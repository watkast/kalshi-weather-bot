# Range-Scalp Bot

*Updated Wed Nov 18 17:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64279 | 56061 | 8218 (124) | 4 | $-17561.59 | -4.3% |
| **+10¢** | 48013 | 38397 | 9616 (165) | 2 | $-16436.46 | -5.4% |
| **+15¢** | 40254 | 29889 | 10365 (210) | 0 | $-14879.19 | -5.9% |
| **+20¢** | 35844 | 24965 | 10879 (265) | 0 | $-13174.27 | -5.9% |
| **+10¢ (15¢ stop)** | 78205 | 78041 | 164 (98) | 0 | $-28801.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 17:41 | +10 stop | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 11-18 17:41 | +20 | ETH | DOWN | 0.58 | 0.85 | 2.43 |
| 11-18 17:41 | +15 | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 11-18 17:41 | +10 | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 11-18 17:41 | +5 | ETH | DOWN | 0.57 | 0.64 | 0.35 |
| 11-18 17:41 | +20 | BNB | DOWN | 0.69 | 0.94 | 2.25 |
| 11-18 17:41 | +10 stop | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-18 17:41 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 11-18 17:41 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.04 |
| 11-18 17:39 | +10 stop | DOGE | DOWN | 0.71 | 0.89 | 1.58 |
| 11-18 17:39 | +20 | DOGE | DOWN | 0.71 | 0.93 | 2.01 |
| 11-18 17:39 | +15 | DOGE | DOWN | 0.71 | 0.89 | 1.58 |
| 11-18 17:39 | +10 | DOGE | DOWN | 0.71 | 0.89 | 1.58 |
| 11-18 17:39 | +5 | DOGE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-18 17:38 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 17:38 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.77 |
| 11-18 17:37 | +15 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 11-18 17:37 | +10 stop | DOGE | DOWN | 0.55 | 0.67 | 0.86 |
| 11-18 17:37 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-18 17:37 | +10 stop | BNB | UP | 0.61 | 0.37 | -2.74 |
| 11-18 17:37 | +5 | BNB | UP | 0.61 | open |  |
| 11-18 17:37 | +5 | HYPE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-18 17:37 | +10 stop | NEAR | UP | 0.58 | 0.37 | -2.45 |
| 11-18 17:37 | +5 | NEAR | UP | 0.58 | open |  |
| 11-18 17:37 | +5 | BTC | UP | 0.63 | open |  |
| 11-18 17:36 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.85 |
| 11-18 17:36 | +10 stop | BTC | UP | 0.62 | 0.42 | -2.35 |
| 11-18 17:36 | +10 | BTC | UP | 0.62 | open |  |
| 11-18 17:36 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 11-18 17:36 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-18 17:35 | +10 stop | ZEC | UP | 0.52 | 0.26 | -2.92 |
| 11-18 17:35 | +5 | ZEC | UP | 0.52 | 0.57 | 0.14 |
| 11-18 17:34 | +10 stop | SOL | UP | 0.69 | 0.46 | -2.63 |
| 11-18 17:34 | +10 | SOL | UP | 0.70 | open |  |
| 11-18 17:34 | +5 | SOL | UP | 0.70 | open |  |
| 11-18 17:34 | +10 stop | DOGE | UP | 0.71 | 0.56 | -1.83 |
| 11-18 17:33 | +10 stop | XRP | UP | 0.60 | 0.45 | -1.86 |
| 11-18 17:33 | +10 stop | HYPE | UP | 0.62 | 0.44 | -2.15 |
| 11-18 17:32 | +10 stop | SOL | UP | 0.64 | 0.75 | 0.79 |
| 11-18 17:32 | +10 | SOL | UP | 0.64 | 0.75 | 0.79 |
