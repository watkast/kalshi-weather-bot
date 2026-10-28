# Range-Scalp Bot

*Updated Wed Oct 28 18:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38342 | 33453 | 4889 (46) | 1 | $-10821.92 | -4.5% |
| **+10¢** | 28599 | 22952 | 5647 (68) | 2 | $-9611.29 | -5.3% |
| **+15¢** | 23924 | 17861 | 6063 (93) | 6 | $-8554.10 | -5.7% |
| **+20¢** | 21225 | 14876 | 6349 (118) | 7 | $-7502.04 | -5.6% |
| **+10¢ (15¢ stop)** | 46919 | 46852 | 67 (35) | 0 | $-17824.98 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 18:33 | +10 stop | BNB | DOWN | 0.57 | 0.24 | -3.61 |
| 10-28 18:33 | +10 stop | NEAR | UP | 0.33 | 0.52 | 1.56 |
| 10-28 18:33 | +20 | NEAR | UP | 0.33 | 0.76 | 4.01 |
| 10-28 18:33 | +15 | NEAR | UP | 0.33 | 0.52 | 1.56 |
| 10-28 18:33 | +10 | NEAR | UP | 0.33 | 0.52 | 1.56 |
| 10-28 18:33 | +5 | NEAR | UP | 0.33 | 0.52 | 1.56 |
| 10-28 18:32 | +10 stop | ZEC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-28 18:32 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 10-28 18:32 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-28 18:32 | +10 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-28 18:32 | +5 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-28 18:32 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-28 18:32 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-28 18:32 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-28 18:32 | +5 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-28 18:32 | +10 stop | XRP | UP | 0.60 | 0.41 | -2.24 |
| 10-28 18:32 | +20 | XRP | UP | 0.60 | 0.83 | 2.03 |
| 10-28 18:32 | +15 | XRP | UP | 0.60 | 0.83 | 2.03 |
| 10-28 18:32 | +10 | XRP | UP | 0.60 | 0.83 | 2.03 |
| 10-28 18:32 | +5 | XRP | UP | 0.60 | 0.83 | 2.03 |
| 10-28 18:32 | +10 stop | BNB | UP | 0.64 | 0.47 | -2.05 |
| 10-28 18:32 | +20 | BNB | UP | 0.63 | open |  |
| 10-28 18:32 | +15 | BNB | UP | 0.63 | open |  |
| 10-28 18:32 | +10 | BNB | UP | 0.63 | 0.74 | 0.79 |
| 10-28 18:32 | +5 | BNB | UP | 0.63 | 0.74 | 0.79 |
| 10-28 18:32 | +10 stop | DOGE | UP | 0.58 | 0.40 | -2.15 |
| 10-28 18:32 | +20 | DOGE | UP | 0.58 | open |  |
| 10-28 18:32 | +15 | DOGE | UP | 0.58 | 0.76 | 1.49 |
| 10-28 18:32 | +10 | DOGE | UP | 0.57 | 0.69 | 0.87 |
| 10-28 18:32 | +5 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 10-28 18:31 | +10 stop | HYPE | UP | 0.46 | 0.24 | -2.51 |
| 10-28 18:31 | +20 | HYPE | UP | 0.46 | open |  |
| 10-28 18:31 | +15 | HYPE | UP | 0.46 | open |  |
| 10-28 18:31 | +10 | HYPE | UP | 0.46 | 0.58 | 0.84 |
| 10-28 18:31 | +5 | HYPE | UP | 0.47 | 0.53 | 0.20 |
| 10-28 18:31 | +5 | SOL | UP | 0.50 | 0.61 | 0.75 |
| 10-28 18:31 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 10-28 18:31 | +20 | BTC | UP | 0.60 | open |  |
| 10-28 18:31 | +15 | BTC | UP | 0.60 | open |  |
| 10-28 18:31 | +10 | BTC | UP | 0.59 | 0.69 | 0.68 |
