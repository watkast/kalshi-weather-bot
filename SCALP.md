# Range-Scalp Bot

*Updated Tue Oct 27 19:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36951 | 32267 | 4684 (44) | 2 | $-10231.58 | -4.4% |
| **+10¢** | 27603 | 22178 | 5425 (66) | 2 | $-9090.74 | -5.2% |
| **+15¢** | 23096 | 17273 | 5823 (90) | 2 | $-8020.28 | -5.5% |
| **+20¢** | 20472 | 14377 | 6095 (115) | 2 | $-6980.16 | -5.4% |
| **+10¢ (15¢ stop)** | 45268 | 45204 | 64 (33) | 0 | $-17225.63 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 19:06 | +5 | BNB | DOWN | 0.65 | open |  |
| 10-27 19:06 | +10 stop | HYPE | UP | 0.69 | 0.84 | 1.21 |
| 10-27 19:05 | +10 stop | BNB | DOWN | 0.64 | 0.45 | -2.25 |
| 10-27 19:05 | +10 | BNB | DOWN | 0.64 | open |  |
| 10-27 19:05 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.38 |
| 10-27 19:04 | +10 stop | BNB | UP | 0.52 | 0.29 | -2.63 |
| 10-27 19:03 | +5 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-27 19:03 | +10 stop | HYPE | UP | 0.65 | 0.48 | -2.04 |
| 10-27 19:02 | +10 stop | NEAR | UP | 0.62 | 0.77 | 1.21 |
| 10-27 19:02 | +15 | NEAR | UP | 0.61 | 0.77 | 1.30 |
| 10-27 19:02 | +10 | NEAR | UP | 0.58 | 0.77 | 1.59 |
| 10-27 19:02 | +5 | NEAR | UP | 0.58 | 0.77 | 1.59 |
| 10-27 19:02 | +10 stop | HYPE | DOWN | 0.62 | 0.38 | -2.78 |
| 10-27 19:02 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-27 19:02 | +15 | HYPE | DOWN | 0.62 | open |  |
| 10-27 19:02 | +10 | HYPE | DOWN | 0.62 | open |  |
| 10-27 19:02 | +5 | HYPE | DOWN | 0.62 | open |  |
| 10-27 19:02 | +10 stop | BNB | DOWN | 0.58 | 0.42 | -1.99 |
| 10-27 19:02 | +20 | BNB | DOWN | 0.58 | open |  |
| 10-27 19:02 | +15 | BNB | DOWN | 0.58 | open |  |
| 10-27 19:02 | +10 | BNB | DOWN | 0.58 | 0.69 | 0.74 |
| 10-27 19:02 | +5 | BNB | DOWN | 0.58 | 0.69 | 0.74 |
| 10-27 19:01 | +10 stop | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-27 19:01 | +20 | DOGE | UP | 0.67 | 0.91 | 2.18 |
| 10-27 19:01 | +15 | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-27 19:01 | +10 | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-27 19:01 | +5 | DOGE | UP | 0.67 | 0.75 | 0.50 |
| 10-27 19:01 | +5 | ETH | UP | 0.67 | 0.74 | 0.40 |
| 10-27 19:01 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-27 19:01 | +20 | SOL | UP | 0.67 | 0.92 | 2.30 |
| 10-27 19:01 | +15 | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-27 19:01 | +10 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-27 19:01 | +5 | SOL | UP | 0.67 | 0.76 | 0.61 |
| 10-27 19:01 | +10 stop | BTC | UP | 0.67 | 0.82 | 1.23 |
| 10-27 19:01 | +20 | BTC | UP | 0.67 | 0.88 | 1.86 |
| 10-27 19:01 | +15 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 10-27 19:01 | +10 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 10-27 19:01 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 10-27 19:01 | +10 stop | ETH | UP | 0.68 | 0.84 | 1.34 |
| 10-27 19:01 | +20 | ETH | UP | 0.68 | 0.88 | 1.76 |
