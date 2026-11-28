# Range-Scalp Bot

*Updated Sat Nov 28 11:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74585 | 65095 | 9490 (171) | 2 | $-19845.77 | -4.2% |
| **+10¢** | 55562 | 44474 | 11088 (217) | 3 | $-18485.99 | -5.3% |
| **+15¢** | 46517 | 34577 | 11940 (275) | 4 | $-16550.13 | -5.7% |
| **+20¢** | 41389 | 28816 | 12573 (343) | 5 | $-14952.63 | -5.8% |
| **+10¢ (15¢ stop)** | 90771 | 90551 | 220 (136) | 0 | $-33491.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 11:12 | +10 stop | BNB | DOWN | 0.57 | 0.40 | -2.05 |
| 11-28 11:12 | +5 | XRP | UP | 0.71 | 0.80 | 0.63 |
| 11-28 11:12 | +10 stop | XRP | UP | 0.55 | 0.80 | 2.20 |
| 11-28 11:12 | +5 | XRP | UP | 0.55 | 0.62 | 0.35 |
| 11-28 11:11 | +10 stop | ETH | DOWN | 0.60 | 0.39 | -2.44 |
| 11-28 11:11 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-28 11:11 | +10 | ETH | DOWN | 0.60 | open |  |
| 11-28 11:11 | +5 | ETH | DOWN | 0.60 | open |  |
| 11-28 11:11 | +10 stop | XRP | DOWN | 0.44 | 0.57 | 0.94 |
| 11-28 11:11 | +5 | XRP | DOWN | 0.44 | 0.57 | 0.94 |
| 11-28 11:10 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.81 |
| 11-28 11:10 | +5 | XRP | DOWN | 0.64 | 0.75 | 0.81 |
| 11-28 11:08 | +10 stop | BNB | DOWN | 0.56 | 0.76 | 1.69 |
| 11-28 11:07 | +10 stop | BNB | UP | 0.50 | 0.60 | 0.65 |
| 11-28 11:07 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-28 11:07 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-28 11:07 | +10 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-28 11:07 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 11-28 11:07 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-28 11:07 | +10 | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-28 11:07 | +5 | SOL | DOWN | 0.66 | 0.81 | 1.20 |
| 11-28 11:06 | +10 stop | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-28 11:06 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 11-28 11:06 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-28 11:06 | +15 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-28 11:06 | +10 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 11-28 11:06 | +5 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 11-28 11:06 | +10 stop | XRP | DOWN | 0.61 | 0.41 | -2.34 |
| 11-28 11:06 | +10 stop | NEAR | DOWN | 0.69 | 0.80 | 0.81 |
| 11-28 11:06 | +10 stop | BNB | DOWN | 0.61 | 0.37 | -2.74 |
| 11-28 11:04 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-28 11:04 | +10 stop | BNB | DOWN | 0.56 | 0.70 | 1.08 |
| 11-28 11:03 | +10 stop | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-28 11:03 | +10 | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 11-28 11:03 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
| 11-28 11:03 | +15 | ETH | DOWN | 0.65 | 0.90 | 2.29 |
| 11-28 11:03 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 11-28 11:02 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-28 11:02 | +20 | BTC | DOWN | 0.69 | open |  |
| 11-28 11:02 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
