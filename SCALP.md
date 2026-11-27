# Range-Scalp Bot

*Updated Fri Nov 27 07:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73548 | 64187 | 9361 (165) | 1 | $-19597.35 | -4.2% |
| **+10¢** | 54805 | 43872 | 10933 (210) | 1 | $-18236.41 | -5.3% |
| **+15¢** | 45894 | 34118 | 11776 (268) | 1 | $-16337.36 | -5.7% |
| **+20¢** | 40841 | 28441 | 12400 (334) | 2 | $-14745.35 | -5.8% |
| **+10¢ (15¢ stop)** | 89575 | 89363 | 212 (129) | 0 | $-33144.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 07:42 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.89 |
| 11-27 07:40 | +10 stop | XRP | UP | 0.62 | 0.88 | 2.30 |
| 11-27 07:39 | +5 | XRP | DOWN | 0.65 | 0.76 | 0.84 |
| 11-27 07:39 | +5 | SOL | UP | 0.62 | 0.73 | 0.79 |
| 11-27 07:38 | +10 stop | XRP | UP | 0.51 | 0.61 | 0.65 |
| 11-27 07:38 | +5 | XRP | UP | 0.52 | 0.58 | 0.24 |
| 11-27 07:38 | +10 stop | SOL | UP | 0.70 | 0.93 | 2.11 |
| 11-27 07:38 | +20 | SOL | UP | 0.70 | 0.93 | 2.11 |
| 11-27 07:38 | +15 | SOL | UP | 0.70 | 0.93 | 2.11 |
| 11-27 07:38 | +10 | SOL | UP | 0.69 | 0.93 | 2.21 |
| 11-27 07:38 | +5 | SOL | UP | 0.69 | 0.77 | 0.52 |
| 11-27 07:37 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.75 |
| 11-27 07:37 | +15 | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-27 07:37 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-27 07:36 | +5 | BNB | UP | 0.39 | 0.68 | 2.57 |
| 11-27 07:36 | +10 stop | ZEC | DOWN | 0.59 | 0.83 | 2.13 |
| 11-27 07:35 | +5 | NEAR | UP | 0.60 | no | -6.17 |
| 11-27 07:34 | +10 stop | ETH | UP | 0.69 | 0.52 | -2.07 |
| 11-27 07:34 | +10 | ETH | UP | 0.69 | no | -7.09 |
| 11-27 07:33 | +20 | DOGE | UP | 0.71 | open |  |
| 11-27 07:33 | +10 stop | ZEC | UP | 0.52 | 0.37 | -1.85 |
| 11-27 07:33 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-27 07:33 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 11-27 07:32 | +10 stop | XRP | UP | 0.66 | 0.79 | 1.02 |
| 11-27 07:32 | +10 stop | BTC | UP | 0.57 | 0.30 | -3.03 |
| 11-27 07:32 | +10 | BTC | UP | 0.57 | open |  |
| 11-27 07:32 | +5 | XRP | UP | 0.65 | 0.75 | 0.73 |
| 11-27 07:32 | +5 | NEAR | UP | 0.51 | 0.56 | 0.14 |
| 11-27 07:32 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.93 |
| 11-27 07:32 | +15 | DOGE | UP | 0.62 | 0.79 | 1.41 |
| 11-27 07:32 | +10 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 11-27 07:32 | +5 | BTC | UP | 0.65 | open |  |
| 11-27 07:32 | +10 stop | BNB | UP | 0.60 | 0.40 | -2.34 |
| 11-27 07:32 | +20 | BNB | UP | 0.59 | no | -6.07 |
| 11-27 07:32 | +15 | BNB | UP | 0.60 | no | -6.17 |
| 11-27 07:32 | +10 | BNB | UP | 0.61 | no | -6.31 |
| 11-27 07:32 | +5 | BNB | UP | 0.60 | 0.66 | 0.22 |
| 11-27 07:32 | +10 stop | SOL | UP | 0.69 | 0.83 | 1.15 |
| 11-27 07:32 | +20 | SOL | UP | 0.66 | 0.87 | 1.86 |
| 11-27 07:32 | +15 | SOL | UP | 0.66 | 0.83 | 1.44 |
