# Range-Scalp Bot

*Updated Wed Oct 21 22:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27817 | 24233 | 3584 (39) | 1 | $-8023.44 | -4.6% |
| **+10¢** | 20905 | 16770 | 4135 (55) | 2 | $-7034.03 | -5.4% |
| **+15¢** | 17510 | 13060 | 4450 (78) | 2 | $-6267.07 | -5.7% |
| **+20¢** | 15502 | 10838 | 4664 (98) | 6 | $-5601.64 | -5.8% |
| **+10¢ (15¢ stop)** | 34156 | 34097 | 59 (32) | 1 | $-12715.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 22:33 | +10 stop | BTC | UP | 0.60 | 0.75 | 1.19 |
| 10-21 22:33 | +10 | BTC | UP | 0.60 | 0.75 | 1.19 |
| 10-21 22:33 | +5 | BTC | UP | 0.60 | 0.69 | 0.58 |
| 10-21 22:32 | +10 stop | BNB | DOWN | 0.59 | open |  |
| 10-21 22:32 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-21 22:32 | +15 | BNB | DOWN | 0.60 | open |  |
| 10-21 22:32 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-21 22:32 | +5 | BNB | DOWN | 0.60 | open |  |
| 10-21 22:31 | +10 stop | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 10-21 22:31 | +20 | ZEC | UP | 0.64 | open |  |
| 10-21 22:31 | +15 | ZEC | UP | 0.64 | 0.80 | 1.31 |
| 10-21 22:31 | +10 | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 10-21 22:31 | +5 | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 10-21 22:31 | +10 | ETH | UP | 0.71 | open |  |
| 10-21 22:31 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 10-21 22:31 | +10 stop | XRP | UP | 0.61 | 0.74 | 1.00 |
| 10-21 22:31 | +20 | XRP | UP | 0.61 | open |  |
| 10-21 22:31 | +15 | XRP | UP | 0.61 | 0.76 | 1.21 |
| 10-21 22:31 | +10 | XRP | UP | 0.61 | 0.74 | 1.00 |
| 10-21 22:31 | +5 | XRP | UP | 0.60 | 0.68 | 0.47 |
| 10-21 22:31 | +10 stop | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-21 22:31 | +20 | SOL | UP | 0.60 | open |  |
| 10-21 22:31 | +15 | SOL | UP | 0.60 | 0.75 | 1.19 |
| 10-21 22:31 | +10 | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-21 22:31 | +5 | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-21 22:31 | +10 stop | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-21 22:31 | +20 | HYPE | UP | 0.64 | open |  |
| 10-21 22:31 | +15 | HYPE | UP | 0.64 | 0.83 | 1.63 |
| 10-21 22:31 | +10 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-21 22:31 | +5 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-21 22:31 | +10 stop | BTC | UP | 0.64 | 0.77 | 1.00 |
| 10-21 22:31 | +20 | BTC | UP | 0.64 | open |  |
| 10-21 22:31 | +15 | BTC | UP | 0.64 | open |  |
| 10-21 22:31 | +10 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 10-21 22:31 | +5 | BTC | UP | 0.63 | 0.70 | 0.38 |
| 10-21 22:27 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-21 22:26 | +10 stop | HYPE | DOWN | 0.68 | 0.44 | -2.74 |
| 10-21 22:26 | +10 stop | ZEC | UP | 0.66 | 0.92 | 2.38 |
| 10-21 22:25 | +5 | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-21 22:25 | +10 stop | BNB | DOWN | 0.56 | 0.69 | 0.97 |
