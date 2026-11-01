# Range-Scalp Bot

*Updated Sun Nov 01 17:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43743 | 38119 | 5624 (64) | 3 | $-12459.79 | -4.5% |
| **+10¢** | 32632 | 26135 | 6497 (85) | 4 | $-11188.74 | -5.5% |
| **+15¢** | 27311 | 20313 | 6998 (112) | 5 | $-10228.74 | -6.0% |
| **+20¢** | 24253 | 16922 | 7331 (146) | 5 | $-9028.58 | -5.9% |
| **+10¢ (15¢ stop)** | 53352 | 53266 | 86 (51) | 0 | $-20138.88 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 17:39 | +10 stop | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 11-01 17:39 | +10 stop | DOGE | UP | 0.41 | 0.55 | 1.05 |
| 11-01 17:39 | +20 | DOGE | UP | 0.42 | open |  |
| 11-01 17:39 | +15 | DOGE | UP | 0.47 | open |  |
| 11-01 17:39 | +10 | DOGE | UP | 0.47 | open |  |
| 11-01 17:39 | +5 | DOGE | UP | 0.47 | 0.55 | 0.44 |
| 11-01 17:38 | +15 | BNB | UP | 0.62 | open |  |
| 11-01 17:37 | +5 | NEAR | UP | 0.63 | open |  |
| 11-01 17:37 | +10 stop | BNB | UP | 0.61 | 0.44 | -2.05 |
| 11-01 17:37 | +5 | BNB | UP | 0.61 | open |  |
| 11-01 17:36 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 11-01 17:35 | +10 stop | SOL | UP | 0.59 | 0.71 | 0.88 |
| 11-01 17:34 | +10 stop | BNB | DOWN | 0.54 | 0.37 | -2.05 |
| 11-01 17:34 | +10 stop | NEAR | UP | 0.59 | 0.43 | -1.95 |
| 11-01 17:34 | +20 | NEAR | UP | 0.59 | open |  |
| 11-01 17:34 | +15 | NEAR | UP | 0.59 | open |  |
| 11-01 17:34 | +10 | NEAR | UP | 0.59 | open |  |
| 11-01 17:34 | +5 | NEAR | UP | 0.59 | 0.64 | 0.16 |
| 11-01 17:33 | +10 stop | ETH | UP | 0.67 | 0.80 | 1.02 |
| 11-01 17:33 | +5 | ETH | UP | 0.67 | 0.75 | 0.50 |
| 11-01 17:33 | +10 stop | SOL | UP | 0.62 | 0.47 | -1.85 |
| 11-01 17:33 | +10 | SOL | UP | 0.62 | 0.79 | 1.41 |
| 11-01 17:33 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 11-01 17:33 | +10 stop | BNB | UP | 0.55 | 0.37 | -2.15 |
| 11-01 17:33 | +10 | BNB | UP | 0.55 | open |  |
| 11-01 17:33 | +5 | BNB | UP | 0.55 | 0.61 | 0.25 |
| 11-01 17:32 | +10 stop | BNB | UP | 0.47 | 0.61 | 1.05 |
| 11-01 17:32 | +20 | BNB | UP | 0.47 | open |  |
| 11-01 17:32 | +15 | BNB | UP | 0.47 | 0.62 | 1.15 |
| 11-01 17:32 | +10 | BNB | UP | 0.47 | 0.61 | 1.05 |
| 11-01 17:32 | +5 | BNB | UP | 0.47 | 0.61 | 1.05 |
| 11-01 17:31 | +10 stop | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 11-01 17:31 | +20 | ZEC | UP | 0.65 | 0.87 | 1.96 |
| 11-01 17:31 | +15 | ZEC | UP | 0.65 | 0.82 | 1.43 |
| 11-01 17:31 | +10 | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 11-01 17:31 | +5 | ZEC | UP | 0.65 | 0.71 | 0.29 |
| 11-01 17:31 | +10 stop | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-01 17:31 | +10 stop | DOGE | UP | 0.62 | 0.79 | 1.41 |
| 11-01 17:31 | +20 | DOGE | UP | 0.62 | 0.83 | 1.83 |
| 11-01 17:31 | +15 | DOGE | UP | 0.62 | 0.79 | 1.41 |
