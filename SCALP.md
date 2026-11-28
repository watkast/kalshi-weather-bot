# Range-Scalp Bot

*Updated Sat Nov 28 10:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74506 | 65031 | 9475 (171) | 1 | $-19788.68 | -4.2% |
| **+10¢** | 55503 | 44432 | 11071 (217) | 1 | $-18421.68 | -5.3% |
| **+15¢** | 46473 | 34551 | 11922 (275) | 1 | $-16474.46 | -5.7% |
| **+20¢** | 41353 | 28798 | 12555 (343) | 1 | $-14880.15 | -5.7% |
| **+10¢ (15¢ stop)** | 90672 | 90452 | 220 (136) | 0 | $-33471.04 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 10:11 | +10 stop | NEAR | DOWN | 0.63 | 0.47 | -1.95 |
| 11-28 10:11 | +15 | NEAR | DOWN | 0.63 | open |  |
| 11-28 10:11 | +10 | NEAR | DOWN | 0.63 | open |  |
| 11-28 10:11 | +5 | NEAR | DOWN | 0.63 | open |  |
| 11-28 10:07 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 11-28 10:07 | +10 | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 11-28 10:07 | +10 stop | BNB | DOWN | 0.58 | 0.89 | 2.85 |
| 11-28 10:07 | +10 stop | SOL | UP | 0.54 | 0.20 | -3.70 |
| 11-28 10:07 | +5 | NEAR | DOWN | 0.66 | 0.75 | 0.60 |
| 11-28 10:07 | +10 stop | XRP | DOWN | 0.71 | 0.86 | 1.27 |
| 11-28 10:07 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.92 |
| 11-28 10:07 | +15 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-28 10:07 | +10 | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-28 10:07 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.43 |
| 11-28 10:06 | +10 stop | NEAR | DOWN | 0.52 | 0.63 | 0.75 |
| 11-28 10:06 | +10 | NEAR | DOWN | 0.52 | 0.63 | 0.75 |
| 11-28 10:06 | +5 | NEAR | DOWN | 0.53 | 0.58 | 0.14 |
| 11-28 10:06 | +10 stop | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-28 10:06 | +20 | ETH | DOWN | 0.67 | 0.90 | 2.08 |
| 11-28 10:06 | +15 | ETH | DOWN | 0.66 | 0.82 | 1.33 |
| 11-28 10:06 | +10 | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-28 10:06 | +5 | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 11-28 10:06 | +10 stop | SOL | UP | 0.62 | 0.75 | 0.99 |
| 11-28 10:05 | +10 stop | BNB | DOWN | 0.61 | 0.38 | -2.63 |
| 11-28 10:05 | +5 | BNB | DOWN | 0.61 | 0.89 | 2.57 |
| 11-28 10:04 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-28 10:04 | +20 | ZEC | DOWN | 0.69 | 0.91 | 1.93 |
| 11-28 10:04 | +15 | ZEC | DOWN | 0.69 | 0.88 | 1.67 |
| 11-28 10:04 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-28 10:04 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-28 10:04 | +5 | BNB | DOWN | 0.62 | 0.69 | 0.38 |
| 11-28 10:02 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 11-28 10:02 | +10 stop | SOL | DOWN | 0.56 | 0.40 | -1.95 |
| 11-28 10:02 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 11-28 10:02 | +15 | SOL | DOWN | 0.60 | 0.79 | 1.61 |
| 11-28 10:02 | +10 | SOL | DOWN | 0.60 | 0.79 | 1.61 |
| 11-28 10:02 | +5 | SOL | DOWN | 0.60 | 0.79 | 1.61 |
| 11-28 10:01 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-28 10:01 | +20 | HYPE | DOWN | 0.71 | 0.92 | 1.89 |
| 11-28 10:01 | +10 stop | BNB | DOWN | 0.67 | 0.52 | -1.84 |
