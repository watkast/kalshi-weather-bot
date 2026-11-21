# Range-Scalp Bot

*Updated Sat Nov 21 07:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67263 | 58713 | 8550 (129) | 1 | $-18008.15 | -4.3% |
| **+10¢** | 50227 | 40234 | 9993 (171) | 1 | $-16722.95 | -5.3% |
| **+15¢** | 42124 | 31350 | 10774 (219) | 1 | $-14992.54 | -5.7% |
| **+20¢** | 37494 | 26172 | 11322 (276) | 1 | $-13321.72 | -5.7% |
| **+10¢ (15¢ stop)** | 81894 | 81728 | 166 (100) | 0 | $-30131.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 07:58 | +10 stop | NEAR | UP | 0.68 | 0.41 | -3.03 |
| 11-21 07:55 | +10 stop | NEAR | UP | 0.65 | 0.79 | 1.12 |
| 11-21 07:52 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-21 07:52 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-21 07:52 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-21 07:52 | +5 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-21 07:51 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-21 07:51 | +20 | HYPE | DOWN | 0.57 | 0.79 | 1.90 |
| 11-21 07:51 | +15 | HYPE | DOWN | 0.57 | 0.73 | 1.27 |
| 11-21 07:51 | +10 | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-21 07:51 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.37 |
| 11-21 07:50 | +5 | NEAR | DOWN | 0.62 | 0.91 | 2.68 |
| 11-21 07:49 | +10 stop | NEAR | DOWN | 0.67 | 0.23 | -4.69 |
| 11-21 07:49 | +20 | NEAR | DOWN | 0.67 | 0.91 | 2.15 |
| 11-21 07:49 | +15 | NEAR | DOWN | 0.66 | 0.91 | 2.25 |
| 11-21 07:49 | +10 | NEAR | DOWN | 0.66 | 0.91 | 2.25 |
| 11-21 07:49 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 11-21 07:48 | +10 stop | NEAR | DOWN | 0.69 | 0.83 | 1.15 |
| 11-21 07:48 | +15 | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 11-21 07:48 | +10 | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 11-21 07:48 | +5 | HYPE | DOWN | 0.61 | 0.78 | 1.40 |
| 11-21 07:47 | +5 | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 11-21 07:47 | +10 stop | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 11-21 07:47 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 11-21 07:47 | +15 | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 11-21 07:47 | +10 | ETH | DOWN | 0.69 | 0.82 | 1.04 |
| 11-21 07:47 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 11-21 07:47 | +5 | BTC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-21 07:47 | +5 | BNB | DOWN | 0.62 | 0.74 | 0.93 |
| 11-21 07:47 | +10 stop | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 11-21 07:47 | +10 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 11-21 07:47 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-21 07:47 | +10 stop | ZEC | UP | 0.51 | 0.31 | -2.29 |
| 11-21 07:47 | +20 | ZEC | UP | 0.49 | open |  |
| 11-21 07:47 | +15 | ZEC | UP | 0.51 | open |  |
| 11-21 07:47 | +10 | ZEC | UP | 0.51 | open |  |
| 11-21 07:47 | +5 | ZEC | UP | 0.51 | open |  |
| 11-21 07:47 | +10 stop | HYPE | DOWN | 0.53 | 0.65 | 0.86 |
| 11-21 07:47 | +20 | HYPE | DOWN | 0.53 | 0.78 | 2.19 |
| 11-21 07:47 | +15 | HYPE | DOWN | 0.52 | 0.78 | 2.29 |
