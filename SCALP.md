# Range-Scalp Bot

*Updated Fri Nov 13 04:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57814 | 50430 | 7384 (101) | 1 | $-15714.12 | -4.3% |
| **+10¢** | 43204 | 34582 | 8622 (133) | 2 | $-14630.48 | -5.4% |
| **+15¢** | 36217 | 26939 | 9278 (167) | 5 | $-13159.70 | -5.8% |
| **+20¢** | 32263 | 22527 | 9736 (217) | 6 | $-11522.82 | -5.7% |
| **+10¢ (15¢ stop)** | 70481 | 70353 | 128 (78) | 2 | $-25968.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 04:25 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 11-13 04:25 | +10 | XRP | DOWN | 0.69 | open |  |
| 11-13 04:25 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.29 |
| 11-13 04:25 | +10 stop | BTC | DOWN | 0.43 | 0.60 | 1.35 |
| 11-13 04:25 | +10 | BTC | DOWN | 0.42 | 0.60 | 1.45 |
| 11-13 04:25 | +5 | BTC | DOWN | 0.42 | 0.60 | 1.45 |
| 11-13 04:25 | +10 stop | BTC | UP | 0.41 | 0.59 | 1.46 |
| 11-13 04:25 | +10 | BTC | UP | 0.42 | 0.59 | 1.35 |
| 11-13 04:25 | +10 stop | SOL | DOWN | 0.63 | open |  |
| 11-13 04:24 | +5 | BTC | UP | 0.59 | 0.65 | 0.27 |
| 11-13 04:24 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-13 04:24 | +20 | DOGE | DOWN | 0.59 | open |  |
| 11-13 04:24 | +15 | DOGE | DOWN | 0.60 | open |  |
| 11-13 04:24 | +10 | DOGE | DOWN | 0.61 | 0.73 | 0.89 |
| 11-13 04:24 | +5 | DOGE | DOWN | 0.61 | 0.73 | 0.89 |
| 11-13 04:24 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 11-13 04:24 | +20 | BNB | DOWN | 0.64 | open |  |
| 11-13 04:24 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-13 04:24 | +10 | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 11-13 04:24 | +5 | BNB | DOWN | 0.64 | 0.73 | 0.59 |
| 11-13 04:24 | +10 stop | SOL | UP | 0.56 | 0.36 | -2.35 |
| 11-13 04:24 | +20 | SOL | UP | 0.55 | open |  |
| 11-13 04:24 | +15 | SOL | UP | 0.56 | open |  |
| 11-13 04:24 | +10 | SOL | UP | 0.56 | open |  |
| 11-13 04:24 | +5 | SOL | UP | 0.57 | open |  |
| 11-13 04:24 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 11-13 04:24 | +20 | XRP | DOWN | 0.64 | open |  |
| 11-13 04:24 | +15 | XRP | DOWN | 0.64 | open |  |
| 11-13 04:24 | +10 | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 11-13 04:24 | +5 | XRP | DOWN | 0.63 | 0.69 | 0.28 |
| 11-13 04:23 | +10 stop | BTC | UP | 0.54 | 0.65 | 0.76 |
| 11-13 04:23 | +20 | BTC | UP | 0.54 | open |  |
| 11-13 04:23 | +15 | BTC | UP | 0.54 | open |  |
| 11-13 04:23 | +10 | BTC | UP | 0.54 | 0.65 | 0.76 |
| 11-13 04:23 | +5 | BTC | UP | 0.54 | 0.59 | 0.15 |
| 11-13 04:23 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 04:23 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-13 04:23 | +15 | ETH | DOWN | 0.68 | 0.85 | 1.45 |
| 11-13 04:23 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-13 04:23 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
