# Range-Scalp Bot

*Updated Thu Nov 12 10:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56783 | 49493 | 7290 (101) | 1 | $-15673.56 | -4.4% |
| **+10¢** | 42435 | 33932 | 8503 (133) | 1 | $-14599.40 | -5.5% |
| **+15¢** | 35579 | 26426 | 9153 (167) | 1 | $-13236.47 | -5.9% |
| **+20¢** | 31692 | 22088 | 9604 (217) | 1 | $-11630.21 | -5.9% |
| **+10¢ (15¢ stop)** | 69244 | 69116 | 128 (78) | 1 | $-25613.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 10:42 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 11-12 10:38 | +10 stop | ETH | UP | 0.71 | 0.49 | -2.53 |
| 11-12 10:38 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-12 10:37 | +10 stop | HYPE | DOWN | 0.58 | 0.74 | 1.28 |
| 11-12 10:36 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.76 |
| 11-12 10:36 | +20 | DOGE | DOWN | 0.69 | 0.89 | 1.78 |
| 11-12 10:36 | +15 | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-12 10:36 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-12 10:36 | +5 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-12 10:36 | +10 stop | BTC | UP | 0.67 | 0.50 | -2.04 |
| 11-12 10:36 | +10 stop | HYPE | DOWN | 0.67 | 0.50 | -2.04 |
| 11-12 10:36 | +20 | HYPE | DOWN | 0.67 | 0.95 | 2.57 |
| 11-12 10:36 | +15 | HYPE | DOWN | 0.67 | 0.95 | 2.57 |
| 11-12 10:36 | +10 | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-12 10:36 | +5 | HYPE | DOWN | 0.67 | 0.74 | 0.40 |
| 11-12 10:35 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 11-12 10:34 | +10 stop | BTC | DOWN | 0.61 | 0.42 | -2.25 |
| 11-12 10:34 | +20 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 11-12 10:34 | +15 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-12 10:34 | +10 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-12 10:34 | +5 | BTC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-12 10:33 | +10 stop | ETH | DOWN | 0.65 | 0.50 | -1.84 |
| 11-12 10:31 | +10 stop | ETH | DOWN | 0.70 | 0.54 | -1.93 |
| 11-12 10:31 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-12 10:31 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-12 10:31 | +10 | ETH | DOWN | 0.70 | open |  |
| 11-12 10:31 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-12 10:31 | +10 stop | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-12 10:31 | +20 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-12 10:31 | +15 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-12 10:31 | +10 | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-12 10:31 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-12 06:31 | +10 stop | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +20 | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +15 | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +10 | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +5 | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +10 stop | XRP | DOWN | 0.71 | no | 2.75 |
| 11-12 06:31 | +15 | XRP | DOWN | 0.71 | no | 2.75 |
| 11-12 06:31 | +10 stop | ZEC | DOWN | 0.65 | no | 3.34 |
