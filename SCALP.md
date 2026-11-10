# Range-Scalp Bot

*Updated Tue Nov 10 09:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54470 | 47510 | 6960 (89) | 2 | $-14875.02 | -4.3% |
| **+10¢** | 40702 | 32582 | 8120 (117) | 3 | $-13821.28 | -5.4% |
| **+15¢** | 34115 | 25360 | 8755 (150) | 5 | $-12596.91 | -5.9% |
| **+20¢** | 30378 | 21195 | 9183 (198) | 6 | $-11000.92 | -5.8% |
| **+10¢ (15¢ stop)** | 66376 | 66266 | 110 (66) | 2 | $-24566.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 09:17 | +5 | XRP | UP | 0.61 | 0.81 | 1.72 |
| 11-10 09:16 | +10 stop | BTC | UP | 0.65 | open |  |
| 11-10 09:16 | +20 | BTC | UP | 0.65 | open |  |
| 11-10 09:16 | +15 | BTC | UP | 0.65 | open |  |
| 11-10 09:16 | +10 | BTC | UP | 0.65 | open |  |
| 11-10 09:16 | +5 | BTC | UP | 0.65 | open |  |
| 11-10 09:16 | +10 stop | BNB | UP | 0.71 | open |  |
| 11-10 09:16 | +20 | BNB | UP | 0.71 | open |  |
| 11-10 09:16 | +15 | BNB | UP | 0.71 | open |  |
| 11-10 09:16 | +10 | BNB | UP | 0.71 | open |  |
| 11-10 09:16 | +5 | BNB | UP | 0.71 | open |  |
| 11-10 09:16 | +10 stop | ETH | UP | 0.66 | 0.79 | 1.02 |
| 11-10 09:16 | +20 | ETH | UP | 0.66 | open |  |
| 11-10 09:16 | +15 | ETH | UP | 0.66 | open |  |
| 11-10 09:16 | +10 | ETH | UP | 0.66 | 0.79 | 1.02 |
| 11-10 09:16 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 11-10 09:16 | +10 stop | ZEC | UP | 0.67 | 0.84 | 1.44 |
| 11-10 09:16 | +20 | ZEC | UP | 0.67 | open |  |
| 11-10 09:16 | +15 | ZEC | UP | 0.67 | 0.84 | 1.44 |
| 11-10 09:16 | +10 | ZEC | UP | 0.67 | 0.84 | 1.44 |
| 11-10 09:16 | +5 | ZEC | UP | 0.67 | 0.74 | 0.40 |
| 11-10 09:16 | +10 stop | XRP | DOWN | 0.47 | 0.18 | -3.19 |
| 11-10 09:16 | +20 | XRP | DOWN | 0.47 | open |  |
| 11-10 09:16 | +15 | XRP | DOWN | 0.47 | open |  |
| 11-10 09:16 | +10 | XRP | DOWN | 0.47 | open |  |
| 11-10 09:16 | +5 | XRP | DOWN | 0.47 | 0.53 | 0.24 |
| 11-10 09:16 | +10 stop | SOL | UP | 0.69 | 0.83 | 1.15 |
| 11-10 09:16 | +20 | SOL | UP | 0.69 | open |  |
| 11-10 09:16 | +15 | SOL | UP | 0.69 | open |  |
| 11-10 09:16 | +10 | SOL | UP | 0.69 | 0.83 | 1.15 |
| 11-10 09:16 | +5 | SOL | UP | 0.68 | 0.73 | 0.20 |
| 11-10 09:03 | +10 stop | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 11-10 09:03 | +20 | ZEC | DOWN | 0.71 | 0.93 | 2.01 |
| 11-10 09:03 | +15 | ZEC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-10 09:03 | +10 | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 11-10 09:03 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-10 08:58 | +10 stop | NEAR | DOWN | 0.70 | 0.42 | -3.13 |
| 11-10 08:58 | +20 | NEAR | DOWN | 0.70 | 0.99 | 2.78 |
| 11-10 08:58 | +15 | NEAR | DOWN | 0.70 | 0.99 | 2.78 |
| 11-10 08:58 | +10 | NEAR | DOWN | 0.70 | 0.99 | 2.78 |
