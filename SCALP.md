# Range-Scalp Bot

*Updated Mon Nov 02 13:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44930 | 39125 | 5805 (66) | 2 | $-12980.81 | -4.6% |
| **+10¢** | 33542 | 26816 | 6726 (87) | 4 | $-11841.63 | -5.6% |
| **+15¢** | 28050 | 20812 | 7238 (114) | 5 | $-10905.24 | -6.2% |
| **+20¢** | 24918 | 17341 | 7577 (149) | 6 | $-9634.55 | -6.2% |
| **+10¢ (15¢ stop)** | 54839 | 54752 | 87 (51) | 0 | $-20738.70 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 13:36 | +10 stop | ETH | DOWN | 0.67 | 0.31 | -3.91 |
| 11-02 13:36 | +15 | ETH | DOWN | 0.67 | open |  |
| 11-02 13:36 | +10 | ETH | DOWN | 0.67 | open |  |
| 11-02 13:36 | +5 | ETH | DOWN | 0.67 | open |  |
| 11-02 13:35 | +10 stop | XRP | DOWN | 0.56 | 0.19 | -3.99 |
| 11-02 13:35 | +10 stop | ZEC | DOWN | 0.62 | 0.12 | -5.25 |
| 11-02 13:34 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-02 13:34 | +10 stop | NEAR | DOWN | 0.71 | 0.14 | -5.94 |
| 11-02 13:34 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-02 13:34 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-02 13:34 | +5 | NEAR | DOWN | 0.71 | 0.80 | 0.63 |
| 11-02 13:34 | +10 stop | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-02 13:34 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-02 13:34 | +10 stop | BTC | DOWN | 0.68 | 0.32 | -3.92 |
| 11-02 13:34 | +10 | BTC | DOWN | 0.68 | open |  |
| 11-02 13:34 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-02 13:34 | +10 stop | ZEC | UP | 0.61 | 0.46 | -1.85 |
| 11-02 13:34 | +10 | ZEC | UP | 0.61 | 0.87 | 2.35 |
| 11-02 13:34 | +5 | ZEC | UP | 0.61 | 0.87 | 2.35 |
| 11-02 13:34 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-02 13:34 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 11-02 13:33 | +10 stop | HYPE | UP | 0.68 | 0.51 | -2.04 |
| 11-02 13:33 | +10 stop | XRP | UP | 0.67 | 0.42 | -2.84 |
| 11-02 13:33 | +10 stop | BNB | DOWN | 0.53 | 0.71 | 1.47 |
| 11-02 13:33 | +10 | BNB | DOWN | 0.53 | 0.71 | 1.47 |
| 11-02 13:33 | +5 | BNB | DOWN | 0.53 | 0.62 | 0.55 |
| 11-02 13:33 | +10 stop | DOGE | UP | 0.64 | 0.33 | -3.43 |
| 11-02 13:33 | +10 | DOGE | UP | 0.64 | 0.94 | 2.73 |
| 11-02 13:33 | +5 | DOGE | UP | 0.64 | 0.72 | 0.48 |
| 11-02 13:33 | +10 stop | SOL | DOWN | 0.54 | 0.74 | 1.68 |
| 11-02 13:33 | +15 | SOL | DOWN | 0.54 | 0.74 | 1.68 |
| 11-02 13:33 | +10 | SOL | DOWN | 0.54 | 0.74 | 1.68 |
| 11-02 13:33 | +5 | SOL | DOWN | 0.55 | 0.74 | 1.58 |
| 11-02 13:32 | +10 stop | ZEC | DOWN | 0.38 | 0.54 | 1.25 |
| 11-02 13:32 | +10 | ZEC | DOWN | 0.38 | 0.54 | 1.25 |
| 11-02 13:32 | +5 | NEAR | DOWN | 0.49 | 0.60 | 0.75 |
| 11-02 13:32 | +10 stop | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-02 13:32 | +10 | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-02 13:32 | +5 | BTC | DOWN | 0.53 | 0.65 | 0.86 |
| 11-02 13:32 | +10 stop | DOGE | DOWN | 0.42 | 0.63 | 1.75 |
