# Range-Scalp Bot

*Updated Sat Oct 31 11:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42183 | 36802 | 5381 (55) | 6 | $-11854.63 | -4.5% |
| **+10¢** | 31452 | 25224 | 6228 (79) | 6 | $-10594.37 | -5.4% |
| **+15¢** | 26302 | 19586 | 6716 (107) | 7 | $-9690.37 | -5.9% |
| **+20¢** | 23360 | 16326 | 7034 (138) | 7 | $-8529.18 | -5.8% |
| **+10¢ (15¢ stop)** | 51461 | 51386 | 75 (41) | 1 | $-19436.57 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 11:34 | +10 stop | SOL | UP | 0.52 | 0.37 | -1.85 |
| 10-31 11:34 | +10 stop | DOGE | UP | 0.52 | open |  |
| 10-31 11:33 | +10 stop | HYPE | UP | 0.66 | 0.41 | -2.87 |
| 10-31 11:32 | +10 stop | XRP | UP | 0.71 | 0.87 | 1.41 |
| 10-31 11:32 | +10 stop | BNB | UP | 0.63 | 0.76 | 1.00 |
| 10-31 11:32 | +10 stop | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-31 11:32 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 10-31 11:32 | +10 stop | ZEC | UP | 0.57 | 0.69 | 0.91 |
| 10-31 11:32 | +20 | ZEC | UP | 0.57 | 0.78 | 1.83 |
| 10-31 11:32 | +15 | ZEC | UP | 0.57 | 0.74 | 1.42 |
| 10-31 11:32 | +10 | ZEC | UP | 0.56 | 0.69 | 0.97 |
| 10-31 11:32 | +5 | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 10-31 11:32 | +5 | SOL | DOWN | 0.56 | 0.62 | 0.25 |
| 10-31 11:31 | +10 stop | SOL | DOWN | 0.57 | 0.35 | -2.54 |
| 10-31 11:31 | +20 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-31 11:31 | +15 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-31 11:31 | +10 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 10-31 11:31 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 10-31 11:31 | +10 stop | HYPE | DOWN | 0.53 | 0.38 | -1.88 |
| 10-31 11:31 | +20 | HYPE | DOWN | 0.54 | open |  |
| 10-31 11:31 | +15 | HYPE | DOWN | 0.56 | open |  |
| 10-31 11:31 | +10 | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-31 11:31 | +5 | HYPE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-31 11:31 | +5 | BTC | DOWN | 0.59 | open |  |
| 10-31 11:31 | +10 stop | ETH | DOWN | 0.48 | 0.30 | -2.13 |
| 10-31 11:31 | +20 | ETH | DOWN | 0.54 | open |  |
| 10-31 11:31 | +15 | ETH | DOWN | 0.55 | open |  |
| 10-31 11:31 | +10 | ETH | DOWN | 0.57 | open |  |
| 10-31 11:31 | +5 | ETH | DOWN | 0.57 | open |  |
| 10-31 11:31 | +10 stop | XRP | DOWN | 0.61 | 0.41 | -2.34 |
| 10-31 11:31 | +20 | XRP | DOWN | 0.61 | open |  |
| 10-31 11:31 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-31 11:31 | +10 | XRP | DOWN | 0.61 | open |  |
| 10-31 11:31 | +5 | XRP | DOWN | 0.61 | open |  |
| 10-31 11:31 | +10 stop | DOGE | DOWN | 0.65 | 0.40 | -2.83 |
| 10-31 11:31 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-31 11:31 | +15 | DOGE | DOWN | 0.65 | open |  |
| 10-31 11:31 | +10 | DOGE | DOWN | 0.65 | open |  |
| 10-31 11:31 | +5 | DOGE | DOWN | 0.65 | open |  |
| 10-31 11:31 | +10 stop | BNB | DOWN | 0.59 | 0.42 | -2.05 |
