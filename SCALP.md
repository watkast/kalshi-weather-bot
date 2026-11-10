# Range-Scalp Bot

*Updated Tue Nov 10 07:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54371 | 47424 | 6947 (89) | 0 | $-14849.27 | -4.3% |
| **+10¢** | 40631 | 32527 | 8104 (117) | 1 | $-13785.44 | -5.4% |
| **+15¢** | 34055 | 25318 | 8737 (150) | 2 | $-12549.84 | -5.9% |
| **+20¢** | 30323 | 21158 | 9165 (198) | 4 | $-10962.57 | -5.8% |
| **+10¢ (15¢ stop)** | 66249 | 66139 | 110 (66) | 1 | $-24496.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 07:32 | +5 | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-10 07:31 | +10 stop | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-10 07:31 | +20 | BTC | UP | 0.62 | 0.83 | 1.83 |
| 11-10 07:31 | +15 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-10 07:31 | +10 | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-10 07:31 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 11-10 07:31 | +10 stop | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 11-10 07:31 | +20 | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 11-10 07:31 | +15 | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 11-10 07:31 | +10 | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 11-10 07:31 | +5 | NEAR | UP | 0.58 | 0.65 | 0.36 |
| 11-10 07:30 | +10 stop | ETH | UP | 0.70 | 0.81 | 0.84 |
| 11-10 07:30 | +20 | ETH | UP | 0.70 | open |  |
| 11-10 07:30 | +15 | ETH | UP | 0.70 | open |  |
| 11-10 07:30 | +10 | ETH | UP | 0.69 | 0.79 | 0.73 |
| 11-10 07:30 | +5 | ETH | UP | 0.69 | 0.77 | 0.52 |
| 11-10 07:30 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-10 07:30 | +20 | SOL | UP | 0.71 | open |  |
| 11-10 07:30 | +15 | SOL | UP | 0.70 | 0.85 | 1.26 |
| 11-10 07:30 | +10 | SOL | UP | 0.70 | 0.81 | 0.84 |
| 11-10 07:30 | +5 | SOL | UP | 0.70 | 0.78 | 0.52 |
| 11-10 07:30 | +10 stop | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-10 07:30 | +20 | XRP | UP | 0.71 | open |  |
| 11-10 07:30 | +15 | XRP | UP | 0.71 | 0.87 | 1.37 |
| 11-10 07:30 | +10 | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-10 07:30 | +5 | XRP | UP | 0.71 | 0.79 | 0.53 |
| 11-10 07:30 | +10 stop | ZEC | UP | 0.68 | open |  |
| 11-10 07:30 | +20 | ZEC | UP | 0.68 | open |  |
| 11-10 07:30 | +15 | ZEC | UP | 0.68 | open |  |
| 11-10 07:30 | +10 | ZEC | UP | 0.68 | open |  |
| 11-10 07:30 | +5 | ZEC | UP | 0.68 | 0.75 | 0.40 |
| 11-10 07:26 | +10 stop | XRP | DOWN | 0.52 | 0.22 | -3.31 |
| 11-10 07:26 | +20 | XRP | DOWN | 0.52 | yes | -5.38 |
| 11-10 07:26 | +15 | XRP | DOWN | 0.52 | yes | -5.38 |
| 11-10 07:26 | +10 | XRP | DOWN | 0.52 | yes | -5.38 |
| 11-10 07:26 | +5 | XRP | DOWN | 0.51 | yes | -5.28 |
| 11-10 07:23 | +10 stop | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-10 07:23 | +10 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 11-10 07:22 | +10 stop | DOGE | UP | 0.65 | 0.84 | 1.64 |
| 11-10 07:21 | +10 stop | HYPE | UP | 0.59 | 0.74 | 1.19 |
