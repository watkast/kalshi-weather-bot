# Range-Scalp Bot

*Updated Sat Oct 31 18:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42570 | 37125 | 5445 (59) | 8 | $-12017.38 | -4.5% |
| **+10¢** | 31740 | 25440 | 6300 (81) | 9 | $-10793.31 | -5.4% |
| **+15¢** | 26547 | 19753 | 6794 (109) | 9 | $-9896.20 | -5.9% |
| **+20¢** | 23577 | 16454 | 7123 (141) | 9 | $-8788.87 | -5.9% |
| **+10¢ (15¢ stop)** | 51945 | 51866 | 79 (44) | 4 | $-19681.13 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 18:11 | +5 | ZEC | DOWN | 0.59 | open |  |
| 10-31 18:10 | +10 stop | XRP | UP | 0.63 | open |  |
| 10-31 18:10 | +10 stop | SOL | UP | 0.68 | open |  |
| 10-31 18:10 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 10-31 18:09 | +10 stop | DOGE | UP | 0.58 | 0.72 | 1.07 |
| 10-31 18:09 | +10 stop | BTC | DOWN | 0.57 | open |  |
| 10-31 18:07 | +10 stop | XRP | UP | 0.67 | 0.51 | -1.94 |
| 10-31 18:07 | +5 | XRP | UP | 0.67 | open |  |
| 10-31 18:07 | +10 stop | ETH | UP | 0.69 | 0.83 | 1.15 |
| 10-31 18:07 | +10 stop | ZEC | UP | 0.59 | 0.83 | 2.13 |
| 10-31 18:07 | +10 stop | BNB | UP | 0.45 | 0.63 | 1.45 |
| 10-31 18:06 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-31 18:05 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-31 18:05 | +10 stop | ETH | UP | 0.55 | 0.67 | 0.86 |
| 10-31 18:05 | +10 stop | BNB | UP | 0.56 | 0.66 | 0.66 |
| 10-31 18:05 | +10 stop | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 10-31 18:04 | +5 | XRP | DOWN | 0.46 | 0.54 | 0.44 |
| 10-31 18:03 | +5 | XRP | DOWN | 0.55 | 0.62 | 0.35 |
| 10-31 18:03 | +5 | NEAR | UP | 0.64 | 0.69 | 0.18 |
| 10-31 18:03 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 10-31 18:03 | +10 stop | ETH | DOWN | 0.60 | 0.42 | -2.15 |
| 10-31 18:03 | +5 | HYPE | UP | 0.63 | open |  |
| 10-31 18:02 | +10 stop | HYPE | UP | 0.60 | 0.44 | -1.99 |
| 10-31 18:02 | +20 | HYPE | UP | 0.60 | open |  |
| 10-31 18:02 | +15 | HYPE | UP | 0.62 | open |  |
| 10-31 18:02 | +10 | HYPE | UP | 0.62 | open |  |
| 10-31 18:02 | +5 | HYPE | UP | 0.62 | 0.67 | 0.17 |
| 10-31 18:02 | +10 stop | SOL | DOWN | 0.62 | 0.46 | -1.95 |
| 10-31 18:02 | +20 | SOL | DOWN | 0.62 | open |  |
| 10-31 18:02 | +15 | SOL | DOWN | 0.62 | open |  |
| 10-31 18:02 | +10 | SOL | DOWN | 0.62 | open |  |
| 10-31 18:02 | +5 | SOL | DOWN | 0.62 | open |  |
| 10-31 18:02 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.94 |
| 10-31 18:02 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-31 18:02 | +15 | XRP | DOWN | 0.65 | open |  |
| 10-31 18:02 | +10 | XRP | DOWN | 0.65 | open |  |
| 10-31 18:02 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 10-31 18:01 | +10 stop | NEAR | DOWN | 0.50 | 0.30 | -2.33 |
| 10-31 18:01 | +20 | NEAR | DOWN | 0.50 | open |  |
| 10-31 18:01 | +15 | NEAR | DOWN | 0.50 | open |  |
