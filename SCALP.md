# Range-Scalp Bot

*Updated Sat Nov 28 09:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74414 | 64953 | 9461 (171) | 0 | $-19746.72 | -4.2% |
| **+10¢** | 55441 | 44385 | 11056 (217) | 0 | $-18383.41 | -5.3% |
| **+15¢** | 46421 | 34514 | 11907 (275) | 0 | $-16437.97 | -5.6% |
| **+20¢** | 41309 | 28771 | 12538 (342) | 0 | $-14836.41 | -5.7% |
| **+10¢ (15¢ stop)** | 90557 | 90337 | 220 (136) | 0 | $-33436.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 08:58 | +10 stop | ETH | DOWN | 0.59 | 0.30 | -3.22 |
| 11-28 08:57 | +5 | SOL | DOWN | 0.71 | 0.89 | 1.58 |
| 11-28 08:56 | +10 stop | BNB | UP | 0.66 | 0.84 | 1.56 |
| 11-28 08:55 | +10 stop | ETH | DOWN | 0.66 | 0.24 | -4.49 |
| 11-28 08:55 | +15 | ETH | DOWN | 0.66 | yes | -6.76 |
| 11-28 08:55 | +10 | ETH | DOWN | 0.66 | yes | -6.76 |
| 11-28 08:55 | +5 | ETH | DOWN | 0.66 | yes | -6.76 |
| 11-28 08:55 | +10 stop | XRP | DOWN | 0.50 | 0.28 | -2.53 |
| 11-28 08:54 | +10 stop | HYPE | UP | 0.71 | 0.88 | 1.47 |
| 11-28 08:54 | +20 | HYPE | UP | 0.71 | 0.92 | 1.88 |
| 11-28 08:54 | +15 | HYPE | UP | 0.70 | 0.88 | 1.57 |
| 11-28 08:54 | +10 | HYPE | UP | 0.70 | 0.88 | 1.57 |
| 11-28 08:54 | +5 | HYPE | UP | 0.69 | 0.75 | 0.31 |
| 11-28 08:53 | +10 stop | XRP | UP | 0.53 | 0.37 | -1.95 |
| 11-28 08:52 | +10 stop | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 11-28 08:52 | +5 | NEAR | DOWN | 0.62 | 0.74 | 0.88 |
| 11-28 08:52 | +10 stop | BNB | DOWN | 0.60 | 0.45 | -1.85 |
| 11-28 08:51 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-28 08:51 | +15 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-28 08:51 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-28 08:51 | +5 | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 11-28 08:51 | +10 | XRP | UP | 0.64 | 0.87 | 2.05 |
| 11-28 08:51 | +10 | BNB | UP | 0.57 | 0.67 | 0.66 |
| 11-28 08:51 | +10 stop | XRP | UP | 0.67 | 0.50 | -2.04 |
| 11-28 08:51 | +5 | XRP | UP | 0.67 | 0.87 | 1.76 |
| 11-28 08:51 | +10 stop | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-28 08:51 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-28 08:51 | +15 | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 11-28 08:51 | +10 | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-28 08:51 | +5 | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-28 08:50 | +10 stop | HYPE | UP | 0.69 | 0.81 | 0.93 |
| 11-28 08:50 | +10 | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 11-28 08:50 | +5 | BNB | UP | 0.67 | 0.84 | 1.44 |
| 11-28 08:50 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 11-28 08:50 | +10 stop | BNB | UP | 0.65 | 0.50 | -1.84 |
| 11-28 08:50 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
| 11-28 08:49 | +10 stop | XRP | DOWN | 0.52 | 0.35 | -2.04 |
| 11-28 08:49 | +10 stop | DOGE | UP | 0.56 | 0.77 | 1.79 |
| 11-28 08:48 | +10 stop | NEAR | DOWN | 0.65 | 0.42 | -2.64 |
| 11-28 08:48 | +20 | NEAR | DOWN | 0.65 | yes | -6.66 |
