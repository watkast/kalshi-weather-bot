# Range-Scalp Bot

*Updated Wed Oct 28 01:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37345 | 32602 | 4743 (45) | 2 | $-10396.48 | -4.4% |
| **+10¢** | 27882 | 22387 | 5495 (67) | 3 | $-9291.52 | -5.3% |
| **+15¢** | 23331 | 17429 | 5902 (91) | 3 | $-8254.94 | -5.6% |
| **+20¢** | 20677 | 14501 | 6176 (116) | 4 | $-7219.53 | -5.6% |
| **+10¢ (15¢ stop)** | 45745 | 45680 | 65 (34) | 2 | $-17457.69 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 01:05 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-28 01:05 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 10-28 01:05 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-28 01:05 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-28 01:05 | +10 | HYPE | DOWN | 0.59 | open |  |
| 10-28 01:05 | +5 | HYPE | DOWN | 0.59 | open |  |
| 10-28 01:04 | +5 | BTC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-28 01:04 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-28 01:04 | +10 stop | ZEC | DOWN | 0.60 | 0.35 | -2.83 |
| 10-28 01:04 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-28 01:04 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-28 01:04 | +10 | ZEC | DOWN | 0.60 | open |  |
| 10-28 01:04 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-28 01:01 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 10-28 01:01 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-28 01:01 | +15 | BTC | DOWN | 0.66 | open |  |
| 10-28 01:01 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-28 01:01 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-28 01:01 | +10 stop | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-28 01:01 | +20 | ZEC | DOWN | 0.66 | 0.89 | 2.07 |
| 10-28 01:01 | +15 | ZEC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-28 01:01 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-28 01:01 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-28 01:01 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-28 01:01 | +20 | BNB | DOWN | 0.65 | 0.85 | 1.75 |
| 10-28 01:01 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 10-28 01:01 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-28 01:01 | +5 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-28 01:01 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-28 01:01 | +20 | ETH | DOWN | 0.69 | open |  |
| 10-28 01:01 | +15 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 10-28 01:01 | +10 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-28 01:01 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.42 |
| 10-28 00:57 | +10 stop | SOL | DOWN | 0.61 | 0.83 | 1.93 |
| 10-28 00:57 | +10 stop | ZEC | DOWN | 0.70 | 0.94 | 2.16 |
| 10-28 00:56 | +15 | SOL | DOWN | 0.54 | 0.83 | 2.62 |
| 10-28 00:56 | +10 stop | NEAR | UP | 0.62 | 0.43 | -2.25 |
| 10-28 00:56 | +10 | NEAR | UP | 0.62 | no | -6.37 |
| 10-28 00:56 | +5 | NEAR | UP | 0.62 | no | -6.37 |
| 10-28 00:55 | +10 stop | SOL | DOWN | 0.71 | 0.52 | -2.23 |
