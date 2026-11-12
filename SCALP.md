# Range-Scalp Bot

*Updated Thu Nov 12 12:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56893 | 49595 | 7298 (101) | 2 | $-15658.45 | -4.4% |
| **+10¢** | 42520 | 34007 | 8513 (133) | 3 | $-14581.83 | -5.5% |
| **+15¢** | 35651 | 26487 | 9164 (167) | 3 | $-13197.00 | -5.9% |
| **+20¢** | 31755 | 22140 | 9615 (217) | 7 | $-11585.45 | -5.8% |
| **+10¢ (15¢ stop)** | 69357 | 69229 | 128 (78) | 2 | $-25620.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 12:34 | +10 stop | SOL | UP | 0.51 | 0.65 | 1.06 |
| 11-12 12:34 | +10 stop | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 11-12 12:34 | +15 | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 11-12 12:34 | +10 | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 11-12 12:34 | +5 | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 11-12 12:34 | +10 stop | ETH | UP | 0.61 | open |  |
| 11-12 12:34 | +10 | ETH | UP | 0.61 | open |  |
| 11-12 12:34 | +5 | ETH | UP | 0.61 | 0.70 | 0.58 |
| 11-12 12:34 | +10 stop | NEAR | UP | 0.54 | 0.72 | 1.47 |
| 11-12 12:34 | +10 | NEAR | UP | 0.54 | 0.72 | 1.47 |
| 11-12 12:34 | +5 | NEAR | UP | 0.55 | 0.72 | 1.37 |
| 11-12 12:33 | +5 | HYPE | UP | 0.67 | open |  |
| 11-12 12:32 | +5 | NEAR | UP | 0.63 | 0.68 | 0.19 |
| 11-12 12:32 | +10 stop | NEAR | UP | 0.55 | 0.68 | 0.96 |
| 11-12 12:32 | +20 | NEAR | UP | 0.55 | open |  |
| 11-12 12:32 | +15 | NEAR | UP | 0.55 | 0.72 | 1.37 |
| 11-12 12:32 | +10 | NEAR | UP | 0.55 | 0.68 | 0.96 |
| 11-12 12:32 | +5 | NEAR | UP | 0.55 | 0.61 | 0.25 |
| 11-12 12:31 | +10 stop | SOL | UP | 0.68 | 0.53 | -1.84 |
| 11-12 12:31 | +20 | SOL | UP | 0.68 | open |  |
| 11-12 12:31 | +15 | SOL | UP | 0.68 | open |  |
| 11-12 12:31 | +10 | SOL | UP | 0.68 | open |  |
| 11-12 12:31 | +5 | SOL | UP | 0.68 | open |  |
| 11-12 12:31 | +10 stop | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 11-12 12:31 | +20 | DOGE | UP | 0.67 | open |  |
| 11-12 12:31 | +15 | DOGE | UP | 0.66 | 0.81 | 1.23 |
| 11-12 12:31 | +10 | DOGE | UP | 0.66 | 0.78 | 0.91 |
| 11-12 12:31 | +5 | DOGE | UP | 0.66 | 0.72 | 0.29 |
| 11-12 12:31 | +10 stop | ETH | UP | 0.64 | 0.74 | 0.69 |
| 11-12 12:31 | +20 | ETH | UP | 0.64 | open |  |
| 11-12 12:31 | +15 | ETH | UP | 0.64 | open |  |
| 11-12 12:31 | +10 | ETH | UP | 0.64 | 0.74 | 0.69 |
| 11-12 12:31 | +5 | ETH | UP | 0.64 | 0.74 | 0.69 |
| 11-12 12:31 | +10 stop | HYPE | UP | 0.71 | open |  |
| 11-12 12:31 | +20 | HYPE | UP | 0.71 | open |  |
| 11-12 12:31 | +15 | HYPE | UP | 0.71 | open |  |
| 11-12 12:31 | +10 | HYPE | UP | 0.71 | open |  |
| 11-12 12:31 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 11-12 12:31 | +10 stop | ZEC | UP | 0.61 | 0.72 | 0.78 |
| 11-12 12:31 | +20 | ZEC | UP | 0.60 | open |  |
