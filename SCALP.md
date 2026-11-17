# Range-Scalp Bot

*Updated Tue Nov 17 07:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62799 | 54778 | 8021 (117) | 6 | $-17093.85 | -4.3% |
| **+10¢** | 46895 | 37507 | 9388 (159) | 5 | $-15995.33 | -5.4% |
| **+15¢** | 39304 | 29179 | 10125 (201) | 6 | $-14550.37 | -5.9% |
| **+20¢** | 35026 | 24411 | 10615 (256) | 8 | $-12717.18 | -5.8% |
| **+10¢ (15¢ stop)** | 76414 | 76258 | 156 (92) | 0 | $-28163.08 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 07:55 | +10 stop | SOL | UP | 0.68 | 0.78 | 0.71 |
| 11-17 07:55 | +15 | SOL | UP | 0.68 | 0.84 | 1.34 |
| 11-17 07:55 | +10 | SOL | UP | 0.69 | 0.82 | 1.04 |
| 11-17 07:55 | +10 stop | HYPE | DOWN | 0.64 | 0.49 | -1.85 |
| 11-17 07:55 | +5 | HYPE | DOWN | 0.64 | 0.83 | 1.59 |
| 11-17 07:54 | +10 stop | ZEC | UP | 0.59 | 0.81 | 1.92 |
| 11-17 07:54 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-17 07:53 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-17 07:52 | +10 stop | BNB | UP | 0.61 | 0.71 | 0.68 |
| 11-17 07:52 | +5 | BNB | UP | 0.61 | 0.71 | 0.68 |
| 11-17 07:52 | +10 stop | ETH | UP | 0.60 | 0.70 | 0.68 |
| 11-17 07:51 | +5 | XRP | UP | 0.61 | 0.70 | 0.58 |
| 11-17 07:51 | +15 | SOL | UP | 0.51 | 0.67 | 1.26 |
| 11-17 07:51 | +15 | HYPE | DOWN | 0.71 | 0.92 | 1.93 |
| 11-17 07:51 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.44 |
| 11-17 07:50 | +15 | BNB | DOWN | 0.50 | open |  |
| 11-17 07:50 | +10 stop | ZEC | DOWN | 0.66 | 0.49 | -2.04 |
| 11-17 07:50 | +5 | SOL | DOWN | 0.61 | open |  |
| 11-17 07:50 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-17 07:49 | +10 stop | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 11-17 07:49 | +10 stop | BNB | UP | 0.52 | 0.62 | 0.65 |
| 11-17 07:49 | +10 stop | SOL | UP | 0.52 | 0.67 | 1.16 |
| 11-17 07:49 | +10 | SOL | UP | 0.52 | 0.67 | 1.16 |
| 11-17 07:49 | +5 | SOL | UP | 0.52 | 0.58 | 0.24 |
| 11-17 07:49 | +10 stop | HYPE | DOWN | 0.70 | 0.50 | -2.33 |
| 11-17 07:49 | +10 | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-17 07:49 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 11-17 07:48 | +10 stop | SOL | DOWN | 0.44 | 0.55 | 0.74 |
| 11-17 07:48 | +20 | SOL | DOWN | 0.44 | open |  |
| 11-17 07:48 | +15 | SOL | DOWN | 0.44 | 0.60 | 1.25 |
| 11-17 07:48 | +10 | SOL | DOWN | 0.43 | 0.55 | 0.84 |
| 11-17 07:48 | +5 | SOL | DOWN | 0.42 | 0.55 | 0.94 |
| 11-17 07:48 | +5 | ETH | DOWN | 0.51 | 0.63 | 0.85 |
| 11-17 07:47 | +10 stop | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-17 07:47 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-17 07:47 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-17 07:47 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-17 07:47 | +5 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-17 07:47 | +10 stop | NEAR | UP | 0.70 | 0.82 | 0.91 |
| 11-17 07:47 | +10 stop | BTC | UP | 0.60 | 0.73 | 0.99 |
