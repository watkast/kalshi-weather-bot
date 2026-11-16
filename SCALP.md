# Range-Scalp Bot

*Updated Mon Nov 16 10:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61901 | 54004 | 7897 (115) | 3 | $-16750.68 | -4.3% |
| **+10¢** | 46242 | 36999 | 9243 (157) | 3 | $-15626.37 | -5.4% |
| **+15¢** | 38749 | 28783 | 9966 (196) | 3 | $-14207.70 | -5.8% |
| **+20¢** | 34549 | 24098 | 10451 (249) | 2 | $-12398.75 | -5.7% |
| **+10¢ (15¢ stop)** | 75356 | 75202 | 154 (90) | 0 | $-27796.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 10:43 | +10 stop | XRP | UP | 0.67 | 0.96 | 2.70 |
| 11-16 10:43 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-16 10:43 | +20 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 11-16 10:42 | +10 stop | DOGE | UP | 0.71 | 0.42 | -3.23 |
| 11-16 10:42 | +15 | DOGE | UP | 0.71 | open |  |
| 11-16 10:42 | +10 | DOGE | UP | 0.71 | open |  |
| 11-16 10:42 | +5 | DOGE | UP | 0.71 | open |  |
| 11-16 10:41 | +10 stop | ZEC | UP | 0.58 | 0.40 | -2.15 |
| 11-16 10:40 | +10 stop | BNB | DOWN | 0.66 | 0.77 | 0.81 |
| 11-16 10:40 | +10 stop | NEAR | UP | 0.71 | 0.46 | -2.83 |
| 11-16 10:40 | +10 stop | ETH | UP | 0.66 | 0.47 | -2.24 |
| 11-16 10:39 | +10 stop | BNB | DOWN | 0.69 | 0.51 | -2.13 |
| 11-16 10:39 | +15 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 11-16 10:39 | +10 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 11-16 10:39 | +5 | BNB | DOWN | 0.69 | 0.77 | 0.52 |
| 11-16 10:38 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 11-16 10:38 | +10 stop | HYPE | UP | 0.62 | 0.76 | 1.10 |
| 11-16 10:38 | +10 stop | DOGE | UP | 0.54 | 0.74 | 1.68 |
| 11-16 10:38 | +15 | DOGE | UP | 0.54 | 0.74 | 1.68 |
| 11-16 10:38 | +10 | DOGE | UP | 0.54 | 0.74 | 1.68 |
| 11-16 10:38 | +5 | DOGE | UP | 0.54 | 0.61 | 0.35 |
| 11-16 10:38 | +10 stop | ETH | DOWN | 0.55 | 0.39 | -1.95 |
| 11-16 10:38 | +20 | ETH | DOWN | 0.56 | 0.77 | 1.79 |
| 11-16 10:38 | +15 | ETH | DOWN | 0.54 | 0.74 | 1.68 |
| 11-16 10:38 | +10 | ETH | DOWN | 0.54 | 0.65 | 0.76 |
| 11-16 10:38 | +5 | ETH | DOWN | 0.55 | 0.62 | 0.35 |
| 11-16 10:38 | +10 stop | ZEC | DOWN | 0.55 | 0.29 | -2.93 |
| 11-16 10:38 | +20 | ZEC | DOWN | 0.53 | 0.75 | 1.88 |
| 11-16 10:38 | +15 | ZEC | DOWN | 0.53 | 0.75 | 1.88 |
| 11-16 10:38 | +10 | ZEC | DOWN | 0.53 | 0.75 | 1.88 |
| 11-16 10:38 | +5 | ZEC | DOWN | 0.53 | 0.75 | 1.88 |
| 11-16 10:38 | +10 stop | DOGE | DOWN | 0.52 | 0.68 | 1.26 |
| 11-16 10:38 | +20 | DOGE | DOWN | 0.52 | 0.72 | 1.67 |
| 11-16 10:38 | +15 | DOGE | DOWN | 0.52 | 0.68 | 1.26 |
| 11-16 10:38 | +10 | DOGE | DOWN | 0.53 | 0.68 | 1.16 |
| 11-16 10:38 | +5 | DOGE | DOWN | 0.53 | 0.68 | 1.16 |
| 11-16 10:38 | +10 stop | XRP | UP | 0.70 | 0.83 | 1.03 |
| 11-16 10:38 | +5 | SOL | DOWN | 0.53 | open |  |
| 11-16 10:36 | +10 stop | HYPE | DOWN | 0.59 | 0.38 | -2.44 |
| 11-16 10:36 | +20 | HYPE | DOWN | 0.59 | 0.88 | 2.65 |
